from django.db import models
from .models_gen import *
from django.utils.functional import cached_property
from django.db.models import Max


@cached_property
def is_hard(self):
    return self.area_id > 12000


QuestData.is_hard = is_hard


class CustomBaseModel(models.Model):
    """docstring for CustomBaseModel"""

    class Meta:
        abstract = True


class QuestRewardDataCustom(CustomBaseModel):
    """docstring for QuestRewardData"""
    # maybe we need to use a wide table
    quest = models.ForeignKey(QuestData, default=None, null=True, on_delete=models.CASCADE)
    equipment = models.ForeignKey(EquipmentData, default=None, null=True, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemData, default=None, null=True, on_delete=models.CASCADE)
    rate = models.FloatField(default=0)


class HatsuneQuestRewardDataCustom(CustomBaseModel):
    """docstring for QuestRewardData"""
    # maybe we need to use a wide table
    quest = models.ForeignKey(HatsuneQuest, default=None, null=True, on_delete=models.CASCADE)
    equipment = models.ForeignKey(EquipmentData, default=None, null=True, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemData, default=None, null=True, on_delete=models.CASCADE)
    rate = models.FloatField(default=0)


class UnitSummary(CustomBaseModel):
    unit = models.OneToOneField(UnitData, primary_key=True, on_delete=models.CASCADE)
    hp = models.FloatField(default=0)
    atk = models.FloatField(default=0)
    magic_str = models.FloatField(default=0)
    def_field = models.FloatField(default=0)
    magic_def = models.FloatField(default=0)
    physical_critical = models.FloatField(default=0)
    magic_critical = models.FloatField(default=0)
    dodge = models.FloatField(default=0)
    hp_recovery_rate = models.FloatField(default=0)
    wave_hp_recovery = models.FloatField(default=0)
    energy_recovery_rate = models.FloatField(default=0)
    wave_energy_recovery = models.FloatField(default=0)
    life_steal = models.FloatField(default=0)

    @classmethod
    def data_tags(cls):
        return [f.name for f in cls._meta.get_fields() if not f.primary_key]

    @classmethod
    def max_level(cls):
        """this method calc the max level each time called, should be store the value somewhere instead of calc"""
        return ExperienceUnit.objects.aggregate(Max("unit_level"))["unit_level__max"]

    @classmethod
    def max_rank(cls):
        """this method calc the max level each time called, should be store the value somewhere instead of calc"""
        return UnitPromotion.objects.aggregate(Max("promotion_level"))["promotion_level__max"]

    @classmethod
    def max_rarity(cls):
        return 5

    @classmethod
    def max_love(cls):
        return 8

class GlobalStatus(object):
    love_status_map = {
        1: 'hp',
        2: 'atk',
        3: 'def_field',
        4: 'magic_str',
        5: 'magic_def',
        6: 'physical_critical',
        7: 'magic_critical',
        8: 'dodge',
        9: 'life_steal',
        10: 'wave_hp_recovery',
        11: 'wave_energy_recovery',
        15: 'hp_recovery_rate',
    }
