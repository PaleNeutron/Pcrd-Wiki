from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, DetailView
from django.shortcuts import get_list_or_404, get_object_or_404
from django.urls import reverse
# Create your views here.
from pcrd_unpack import models
from django.http import JsonResponse, HttpResponse, Http404
from django.core import serializers

class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context

class UnitJsonView(JSONResponseMixin, TemplateView):
    """docstring for UnitJsonView"""
    def render_to_response(self, context, **response_kwargs):

        response_context = {}
        unit_id = context["unit_id"]
        try:
            unit_data = models.UnitRarity.objects.filter(unit_id=unit_id).values()
        except models.UnitRarity.DoesNotExist:
            raise Http404("unit not found")

        try:
            unit_rank_data = models.UnitPromotionStatus.objects.filter(unit_id=unit_id).values()
        except models.UnitRarity.DoesNotExist:
            raise Http404("unit not found")

        response_context["unit_data"] = list(unit_data)
        response_context["unit_rank_data"] = list(unit_rank_data)

        return JsonResponse(response_context)
