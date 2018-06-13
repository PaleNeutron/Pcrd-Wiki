from django.db import models
from .models_gen import *
from django.utils.functional import cached_property
from django.db.models import Max
from django.contrib.auth.models import User

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
    energy_reduce_rate = models.FloatField(default=0)

    @classmethod
    def data_tags(cls):
        return [f.name for f in cls._meta.get_fields() if not f.primary_key]

    @classmethod
    def max_level(cls):
        """this method calc the max level each time called, should be store the value somewhere instead of calc"""
        return ExperienceUnit.objects.aggregate(Max("unit_level"))["unit_level__max"] - 1

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

    @cached_property
    def position(self):
        return self.unit.search_area_width


class Team(CustomBaseModel):
    UNITS_NUM = 5

    unit_1 = models.ForeignKey(UnitData, on_delete=models.CASCADE, related_name="unit_1")
    unit_2 = models.ForeignKey(UnitData, on_delete=models.CASCADE, related_name="unit_2")
    unit_3 = models.ForeignKey(UnitData, on_delete=models.CASCADE, related_name="unit_3")
    unit_4 = models.ForeignKey(UnitData, on_delete=models.CASCADE, related_name="unit_4")
    unit_5 = models.ForeignKey(UnitData, on_delete=models.CASCADE, related_name="unit_5")
    rarity_1 = models.IntegerField(default=1)
    rarity_2 = models.IntegerField(default=1)
    rarity_3 = models.IntegerField(default=1)
    rarity_4 = models.IntegerField(default=1)
    rarity_5 = models.IntegerField(default=1)

    def __str__(self):
        return "{} {}, {} {}, {} {}, {} {}, {} {}".format(
            self.unit_1.unit_name,
            self.rarity_1,
            self.unit_2.unit_name,
            self.rarity_2,
            self.unit_3.unit_name,
            self.rarity_3,
            self.unit_4.unit_name,
            self.rarity_4,
            self.unit_5.unit_name,
            self.rarity_5,
        )

    @property
    def team_list(self):
        return [self.unit_1.unit_id, self.unit_2.unit_id, self.unit_3.unit_id, self.unit_4.unit_id, self.unit_5.unit_id, ]

    @property
    def rarity_list(self):
        return [self.rarity_1, self.rarity_2, self.rarity_3, self.rarity_4, self.rarity_5, ]

    @classmethod
    def get_team(cls, team_list, rarity_list):
        kw = cls._list_to_key(team_list, rarity_list)
        team = cls.objects.get_or_create(**kw)
        return team

    @classmethod
    def _list_to_key(cls, team_list, rarity_list):
        unit_key = [("unit_{}".format(i+1), UnitData.objects.get(unit_id=u)) for i, u in enumerate(team_list)]
        rarity_key = [("rarity_{}".format(i+1), r) for i, r in enumerate(rarity_list)]
        return dict(unit_key+rarity_key)

class Solution(CustomBaseModel):
    left_team = models.ForeignKey(Team, default=None, null=True, on_delete=models.CASCADE, related_name="left_team")
    right_team = models.ForeignKey(Team, default=None, null=True, on_delete=models.CASCADE, related_name="right_team")
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    pub_data = models.DateField(auto_now=True)

    def __str__(self):
        return "Solution {}".format(str(self.id))

class SolutionComment(CustomBaseModel):
    comment = models.TextField(max_length=1000)
    user = models.IntegerField(default=1)
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE)

    def get_user(self):
        return User.objects.get(id=self.user)

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
