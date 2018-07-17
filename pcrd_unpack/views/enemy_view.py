from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import TemplateView, View, ListView, DetailView
from django.shortcuts import get_list_or_404, get_object_or_404
from itertools import zip_longest
from django.http import HttpResponseNotFound
from django.urls import reverse
# Create your views here.
from pcrd_unpack import models
from collections import OrderedDict
from pcrd_unpack.utils import skill_utility


class EnemyListView(TemplateView):
    """docstring for EnemyListView"""
    template_name = "pcrd_unpack/enemy/enemy_list.html"

    def get_context_data(self, **kwargs):
        context = {}
        enemies = models.EventEnemyParameter.objects.all()
        context["enemies"] = enemies
        return context


