from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, DetailView
from django.shortcuts import get_list_or_404, get_object_or_404
from django.urls import reverse
# Create your views here.
from pcrd_unpack import models
from collections import OrderedDict


class EquipmentView(TemplateView):
    """docstring for """
    template_name = "pcrd_unpack/equipment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        eq = get_object_or_404(models.EquipmentData, pk=self.kwargs["equipment_id"])
        context['equipment'] = eq
        drops = eq.questrewarddatacustom_set.all().order_by('quest__area_id')
        quests = [i.quest for i in drops]
        quests.sort(key=lambda x: x.area_id)
        # before python3.6 dict do not keep order, use OrderedDict
        context['drop_info'] = OrderedDict(zip(quests, [q.questrewarddatacustom_set.order_by('-rate') for q in quests]))
        if eq.craft_flg:
            cinfo = get_object_or_404(models.EquipmentCraft, pk=self.kwargs["equipment_id"])
            context["craft_info"] = cinfo
            components = {}
            for i in range(1, 11):
                eqid = getattr(cinfo, "condition_equipment_id_{}".format(i))
                eq_num = getattr(cinfo, "consume_num_{}".format(i))
                if eqid:
                    components[eqid] = eq_num
            context["components"] = components
        return context


class EquipmentListView(ListView):
    """docstring for Equi"""
    template_name = "pcrd_unpack/equipment_list.html"

    # model = models.EquipmentData

    def get_queryset(self):
        return models.EquipmentData.objects.order_by("-promotion_level")


class ItemView(TemplateView):
    """docstring for """
    template_name = "pcrd_unpack/item.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = get_object_or_404(models.ItemData, pk=self.kwargs["item_id"])
        context['item'] = item
        drops = item.questrewarddatacustom_set.all().order_by('quest__area_id')
        quests = [i.quest for i in drops]
        context['drop_info'] = OrderedDict(zip(quests, [q.questrewarddatacustom_set.order_by('-rate') for q in quests]))
        return context


# class ItemListView(ListView):
#     """docstring for Equi"""
#     template_name = "pcrd_unpack/item_list.html"
#     # model = models.EquipmentData
#
#     def get_queryset(self):
#         return models.ItemData.objects.order_by("-promotion_level")


class QuestAreaListView(ListView):
    """docstring for QuestAreaListView"""
    template_name = "pcrd_unpack/quests_list.html"
    model = models.QuestAreaData


class QuestAreaDetailView(TemplateView):
    """docstring for QuestAreaDetailView"""
    template_name = "pcrd_unpack/quest_area_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        area_id = self.kwargs["area_id"]
        area = get_object_or_404(models.QuestAreaData.objects, pk=area_id)
        context["area_title"] = area.area_name
        quests_in_charpter = models.QuestData.objects.filter(area_id=area_id)
        context["quests_in_charpter"] = quests_in_charpter
        context["quest_reward"] = {}
        for q in quests_in_charpter:
            context["quest_reward"][q] = q.questrewarddatacustom_set.order_by('-rate')
        return context


class UnitListView(ListView):
    """docstring for UnitListView"""
    template_name = "pcrd_unpack/unit_list.html"
    model = models.UnitData

    def get_queryset(self, **hints):
        return self.model.objects.exclude(comment__isnull=True).order_by("-rarity")


class UnitDetailView(TemplateView):
    """docstring for UnitDetailView"""
    template_name = "pcrd_unpack/unit_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        unit_id = kwargs["unit_id"]
        unit_data = get_object_or_404(models.UnitData, pk=unit_id)
        unit_data.comment = unit_data.comment.replace("\\n", "\n")
        unit_profile = get_object_or_404(models.UnitProfile, pk=unit_id)
        unit_promotion = get_list_or_404(models.UnitPromotion, pk=unit_id)
        unit_skill = get_object_or_404(models.UnitSkillData, pk=unit_id)
        skills = [
            get_object_or_404(models.SkillData, skill_id=getattr(unit_skill, f.name))
            for f in type(unit_skill)._meta.get_fields()
            if (not f.primary_key and getattr(unit_skill, f.name) != 0)
        ]
        unit_skills = {skill: self.get_skill_actions(skill) for skill in skills}
        context["unit_data"] = unit_data
        context["unit_profile"] = unit_profile
        context["unit_promotion"] = unit_promotion
        context["unit_skills"] = unit_skills

        return context

    def get_skill_actions(self, skill: models.SkillData):
        actions = [get_object_or_404(models.SkillAction, action_id=getattr(skill, f.name))
                   for f in type(skill)._meta.get_fields()
                   if not f.primary_key and f.name.startswith("action") and getattr(skill, f.name) != 0]
        for a in actions:
            if a.action_type in [90, 26]:
                a.action_value_1 = a.action_value_2
                a.action_value_2 = a.action_value_3
                a.action_value_3 = 0
                a.action_value_4 = 0
        return actions

def handler404(request, exception):
    return render(request, 'pcrd_unpack/errors/404.html', locals())