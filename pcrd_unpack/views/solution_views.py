from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, DetailView
from django.shortcuts import get_list_or_404, get_object_or_404
from itertools import zip_longest
from django.urls import reverse
# Create your views here.
from pcrd_unpack import models
from collections import OrderedDict

class CreateSolutionView(TemplateView):
    template_name = "pcrd_unpack/create_solution.html"
    def get_context_data(self, **kwargs):
        # units = [models.UnitData.objects.get(unit_id=100101),
        #          models.UnitData.objects.get(unit_id=100102),]
        context = {
            'units': models.UnitData.objects.order_by('search_area_width').exclude(comment__exact="").exclude(unit_id__gt=200000),
            "left":[
                {
                    'unit':100101,
                    'rarity': 3,
                },
                {
                    'unit': 100102,
                    'rarity': 3,
                },                {
                    'unit': 100102,
                    'rarity': 3,
                },                {
                    'unit': 100102,
                    'rarity': 3,
                },                {
                    'unit': 100102,
                    'rarity': 3,
                },
            ],
            "right":[
                {
                    'unit':100101,
                    'rarity': 3,
                },
                {
                    'unit': 100102,
                    'rarity': 3,
                },                {
                    'unit': 100102,
                    'rarity': 3,
                },                {
                    'unit': 100102,
                    'rarity': 3,
                },                {
                    'unit': 100102,
                    'rarity': 3,
                },
            ],
            "rarity_set": range(models.UnitSummary.max_rarity(), 0, -1),
        }
        return context