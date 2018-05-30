import json

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, DetailView
from django.shortcuts import get_list_or_404, get_object_or_404
from itertools import zip_longest
from django.urls import reverse
# Create your views here.
from pcrd_unpack import models
from collections import OrderedDict

class SolutionView(TemplateView):
    template_name = "pcrd_unpack/solution/create_solution.html"
    def get_context_data(self, **kwargs):
        solution_id = kwargs["solution_id"]
        solution = get_object_or_404(models.Solution, id=solution_id)
        context = {
            'units': models.UnitData.objects.order_by('search_area_width').exclude(comment__exact="").exclude(unit_id__gt=200000),
            "rarity_set": range(models.UnitSummary.max_rarity(), 0, -1),
            "left_team":solution.left_team.team_list,
            "left_rarity": solution.left_team.rarity_list,
            "right_team":solution.right_team.team_list,
            "right_rarity": solution.right_team.rarity_list,
        }
        return context

class CreateSolutionView(TemplateView):
    template_name = "pcrd_unpack/solution/create_solution.html"
    def get_context_data(self, **kwargs):
        # units = [models.UnitData.objects.get(unit_id=100101),
        #          models.UnitData.objects.get(unit_id=100102),]
        context = {
            'units': models.UnitData.objects.order_by('search_area_width').exclude(comment__exact="").exclude(unit_id__gt=200000),
            "left_team":[],
            "left_rarity": [models.UnitSummary.max_rarity()]*models.Team.UNITS_NUM,
            "right_team":[],
            "right_rarity": [models.UnitSummary.max_rarity()]*models.Team.UNITS_NUM,
            "rarity_set": range(models.UnitSummary.max_rarity(), 0, -1),
        }
        return context

class SolutionIndexView(TemplateView):
    """docstring for SolutionIndexView"""
    template_name = "pcrd_unpack/solution/solution_index.html"
    def get_context_data(self, **kwargs):
        s_to_show = models.Solution.objects.order_by("-up_vote", "down_vote")[:5]
        context = {
            'units': models.UnitData.objects.order_by('search_area_width').exclude(comment__exact="").exclude(
                unit_id__gt=200000),
            "rarity_set": range(models.UnitSummary.max_rarity(), 0, -1),
            "solution": s_to_show
        }
        return context


def create_solution_handler(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        if True:
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            data = json.loads(request.body.decode())
            for i in data:
                if len(i) != models.Team.UNITS_NUM or None in i:
                     return HttpResponseForbidden()
            create_solution(data["left_team"], data["left_rarity"], data["right_team"], data["right_rarity"])
            r = reverse("pcrd_unpack:index")
            return HttpResponse(str(r))

def create_solution(left_team:list, left_rarity:list, right_team:list, right_rarity:list):
    lt, created = models.Team.get_team(left_team, left_rarity)
    rt, created = models.Team.get_team(right_team, right_rarity)
    s = models.Solution(left_team=lt, right_team=rt)
    s.save()
    return s.id