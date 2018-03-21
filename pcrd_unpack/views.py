from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, DetailView
from django.shortcuts import get_list_or_404, get_object_or_404
from . import coop
# Create your views here.
from . import models

class EqupimentView(TemplateView):
    """docstring for """
    template_name = "pcrd_unpack/equipment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quests'] = coop.get_drop_string()
        return context

class QuestListView(ListView):
    """docstring for QuestView"""
    template_name = "pcrd_unpack/quests_list.html"
    model = models.QuestAreaData

class QuestDetailView(TemplateView):
    """docstring for QuestDetailView"""
    template_name = "pcrd_unpack/quest_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context =



