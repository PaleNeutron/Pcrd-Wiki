from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, DetailView
from django.shortcuts import get_list_or_404, get_object_or_404
from django.urls import reverse
# Create your views here.
from pcrd_unpack import models
from django.http import JsonResponse, HttpResponse, Http404
from django.db.models import Max, QuerySet

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
        response_context = self.get_unit_data(context["unit_id"])
        return JsonResponse(response_context)

    def get_unit_data(self, unit_id=0):
        response_context = {}
        try:
            unit_data = models.UnitRarity.objects.filter(unit_id=unit_id).values()
        except models.UnitRarity.DoesNotExist:
            raise Http404("unit not found")

        try:
            unit_rank_data = models.UnitPromotionStatus.objects.filter(unit_id=unit_id).values()
        except models.UnitRarity.DoesNotExist:
            raise Http404("unit not found")

        try:
            unit_promotion_data_query = models.UnitPromotion.objects.filter(unit_id=unit_id).values()
            related_equipments = []
            unit_promotion_data =[]
            for i in unit_promotion_data_query:
                temp = []
                for j in range(1,7):
                    eq_id = i['equip_slot_{}'.format(j)]
                    related_equipments.append(eq_id)
                    temp.append(eq_id)
                unit_promotion_data.append(temp)
        except models.UnitRarity.DoesNotExist:
            raise Http404("unit not found")

        try:
            equipment_data = models.EquipmentData.objects.filter(equipment_id__in=related_equipments).values()
            equipment_data = {e["equipment_id"]: e for e in equipment_data}
        except models.UnitRarity.DoesNotExist:
            raise Http404("unit not found")


        try:
            equipment_enhance = models.EquipmentEnhanceRate.objects.filter(equipment_id__in=related_equipments).values()
            equipment_enhance = {e["equipment_id"]: e for e in equipment_enhance}
        except models.UnitRarity.DoesNotExist:
            raise Http404("unit not found")

        # enhance_table
        max_enhance = models.EquipmentEnhanceData.objects.aggregate(Max('promotion_level'))["promotion_level__max"]
        enhance_table = {i: models.EquipmentEnhanceData.objects.filter(promotion_level__exact=i).aggregate(Max('equipment_enhance_level'))["equipment_enhance_level__max"]
                         for i in range(2, max_enhance +1 )}

        # get love status bonus
        ls = models.CharaStoryStatus.objects.filter(chara_id_1__exact=int(unit_id / 100)).order_by('story_id')
        love_table = [self.reverse_love_status(l) for l in ls]
        response_context["unit_data"] = list(unit_data)
        response_context["unit_rank_data"] = list(unit_rank_data)
        response_context["unit_promotion_data"] = unit_promotion_data
        response_context["equipment_data"] = equipment_data
        response_context["equipment_enhance"] = equipment_enhance
        response_context["enhance_table"] = enhance_table
        response_context["love_table"] = love_table
        return response_context

    def reverse_love_status(self, love_status):
        ls_talbe = {}
        for i in range(1, 6):
            st = getattr(love_status, "status_type_{}".format(i))
            if st != 0:
                ls_talbe[models.GlobalStatus.love_status_map[st]] = getattr(love_status, "status_rate_{}".format(i))
        return ls_talbe