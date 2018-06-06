import json

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, request
from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, DetailView
from django.shortcuts import get_list_or_404, get_object_or_404
from itertools import zip_longest
from django.urls import reverse
# Create your views here.
from pcrd_unpack import models
from collections import OrderedDict
import base64

def team_base_context():
    context = {
        'units': models.UnitData.objects.order_by('search_area_width').exclude(comment__exact="").exclude(unit_id__gt=200000),
        "rarity_set": range(models.UnitSummary.max_rarity(), 0, -1),
    }
    return context

class SolutionView(TemplateView):
    template_name = "pcrd_unpack/solution/create_solution.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs, uri = request.build_absolute_uri())

        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        solution_id = kwargs["solution_id"]
        solution = get_object_or_404(models.Solution, id=solution_id)
        context = {
            **team_base_context(),
            **{
                "left_team":solution.left_team.team_list,
                "left_rarity": solution.left_team.rarity_list,
                "right_team":solution.right_team.team_list,
                "right_rarity": solution.right_team.rarity_list,
                "share_link": kwargs["uri"],
                "solution": solution,
            },
        }
        return context

class CreateSolutionView(TemplateView):
    template_name = "pcrd_unpack/solution/create_solution.html"
    def get_context_data(self, **kwargs):
        # units = [models.UnitData.objects.get(unit_id=100101),
        #          models.UnitData.objects.get(unit_id=100102),]
        context = {
            **team_base_context(),
            **{
                "left_team":[""]*models.Team.UNITS_NUM,
                "left_rarity": [models.UnitSummary.max_rarity()]*models.Team.UNITS_NUM,
                "right_team":[""]*models.Team.UNITS_NUM,
                "right_rarity": [models.UnitSummary.max_rarity()]*models.Team.UNITS_NUM,
            },
        }
        return context

class SolutionIndexView(TemplateView):
    """docstring for SolutionIndexView"""
    template_name = "pcrd_unpack/solution/solution_index.html"
    def get_context_data(self, **kwargs):
        s_to_show = models.Solution.objects.order_by("-up_vote", "down_vote")[:5]
        context = {
                **team_base_context(),
                **{
                "solution": s_to_show
            },
        }
        return context

class SolutionSearchView(TemplateView):
    template_name = "pcrd_unpack/solution/solution_search.html"
    def post(self, request, *args, **kwargs):
        if request.body:
            data = json.loads(request.body.decode())
            context = self.get_context_data(**kwargs, data = data)
        else:
            context = self.get_context_data(**kwargs)

        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        s_to_show = []
        if 'data' in kwargs:
            team = kwargs["data"]["team"]
            team_dict = {"right_team__unit_{}".format(i+1): u for i, u in enumerate(team) if u != ""}

            if team_dict:
                s_to_show = models.Solution.objects.filter(**team_dict).order_by("-up_vote", "down_vote")[:5]
        context = {
            **team_base_context(),
            **{
                "left_team":[""]*models.Team.UNITS_NUM,
                "left_rarity": [models.UnitSummary.max_rarity()]*models.Team.UNITS_NUM,
                "solution": s_to_show
            },
        }
        return context


def create_solution_handler(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # check whether it's valid:

        data = json.loads(request.body.decode())
        for key, value in data.items():
            if len(value) != models.Team.UNITS_NUM or None in value:
                 return HttpResponseForbidden()
        sid = create_solution(data["left_team"], data["left_rarity"], data["right_team"], data["right_rarity"])
        r = reverse("pcrd_unpack:solution", kwargs={"solution_id":sid})
        return HttpResponse(r)

def vote(request):
    if request.method == 'GET':
        target = request.META["HTTP_REFERER"].split("/")[-1]
        method = request.GET["method"]
        solution = get_object_or_404(models.Solution, id=target)
        if method == "up_vote":
            solution.up_vote += 1
        elif method == "down_vote":
            solution.down_vote += 1
        solution.save()
        return HttpResponse()


def create_solution(left_team:list, left_rarity:list, right_team:list, right_rarity:list):
    lt, created = models.Team.get_team(left_team, left_rarity)
    rt, created = models.Team.get_team(right_team, right_rarity)
    s = models.Solution(left_team=lt, right_team=rt)
    s.save()
    return s.id