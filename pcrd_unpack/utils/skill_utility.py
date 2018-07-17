# based on SkillDefine.cs and SkillUtility.cs

import enum
from pcrd_unpack import models

class ActionType(enum.IntEnum):
    ATTACK = 1
    MOVE = 2
    KNOCK = 3
    HEAL = 4
    CURE = 5
    BARRIER = 6
    REFLEXIVE = 7
    CHANGE_SPEED = 8
    SLIP_DAMAGE = 9
    BUFF_DEBUFF = 10
    CHARM = 11
    BLIND = 12
    SILENCE = 13
    MODE_CHANGE = 14
    SUMMON = 15
    CHARGE_ENERGY = 16
    TRIGER = 17
    DAMAGE_CHARGE = 18
    CHARGE = 19
    DECOY = 20
    NO_DAMAGE = 21
    CHANGE_PATTERN = 22
    IF_FOR_CHILDREN = 23
    REVIVAL = 24
    CONTINUOUS_ATTACK = 25
    GIVE_VALUE_AS_ADDITIVE = 26
    GIVE_VALUE_AS_MULTIPLE = 27
    IF_FOR_ALL = 28
    SEARCH_AREA_CHANGE = 29
    DESTROY = 30
    CONTINUOUS_ATTACK_NEARBY = 31
    ENCHANT_LIFE_STEAL = 32
    ENCHANT_STRIKE_BACK = 33
    ACCUMULATIVE_DAMAGE = 34
    SEAL = 35
    ATTACK_FIELD = 36
    HEAL_FIELD = 37
    CHANGE_PARAMETER_FIELD = 38
    SLIP_DAMAGE_FIELD = 39
    CHANGE_SPEED_FIELD = 40
    UB_CHANGE_TIME = 41
    LOOP_TRIGGER = 42
    IF_HAS_TARGET = 43
    WAVE_START_IDLE = 44
    SKILL_EXEC_COUNT = 45
    RATIO_DAMAGE = 46
    UPPER_LIMIT_ATTACK = 47
    REGENERATION = 48
    PASSIVE = 49

def get_action_result(a: models.SkillAction):
    try:
        a.action_name = ActionType(a.action_type)
    except:
        a.action_name = None

    if a.action_type in [1, 8, 9, 11, 12, 13, 25, 32, 38, 39, 40, 47, ]:
        if a.action_value_2:
            a.action_value_1 = "{} + {}*skill_level".format(a.action_value_1, a.action_value_2)
        if a.action_value_4:
            a.action_value_3 = "{} + {}*skill_level".format(a.action_value_3, a.action_value_4)
    elif a.action_type in [4, 10, 24, 29, 31, 34, ]:
        if a.action_value_3:
            a.action_value_2 = "{} + {}*skill_level".format(a.action_value_2, a.action_value_3)
        if a.action_value_5:
            a.action_value_4 = "{} + {}*skill_level".format(a.action_value_4, a.action_value_5)
    elif a.action_type in [5, 6, 14, 16, 17, 18, 19, 20, 21, 33, 46, ]:
        if a.action_value_2:
            a.action_value_1 = "{} + {}*skill_level".format(a.action_value_1, a.action_value_2)
    elif a.action_type in [90, 91, 26, 15, 27]:
        if a.action_value_3:
            a.action_value_2 = "{} + {}*skill_level".format(a.action_value_2, a.action_value_3)
    elif a.action_type == 27:
        pass
    elif a.action_type in [36, 37, 48]:
        if a.action_value_2:
            a.action_value_1 = "{} + {}*skill_level".format(a.action_value_1, a.action_value_2)
        if a.action_value_4:
            a.action_value_3 = "{} + {}*skill_level".format(a.action_value_3, a.action_value_4)
        if a.action_value_6:
            a.action_value_5 = "{} + {}*skill_level".format(a.action_value_5, a.action_value_6)
    else:
        pass

    # manual patches
    if a.action_type == 2:
        factor_static = a.action_value_1

    # KNOCK
    # elif a.action_type == 3:
    #     factor_static = a.action_value_1
    elif a.action_type in [9, 12]:
        # I don't know why, but
        # type 9 is DOT
        # type 10 is self-buff
        # type 12 is de-buff
        # type 34 is accumulated self-buff or buff forever
        # which are not affected by atk
        factor_atk = 0
        factor_atk_level = 0

    a.result = ""
    a.time = ""
    if a.action_value_1:
        a.result += str(a.action_value_1)
    if a.action_value_3:
        a.result += " + {} * atk".format(a.action_value_3)

    # patch for individual skill
    # CHANGE_SPEED
    if a.action_type in [ActionType.CHANGE_SPEED, ActionType.SLIP_DAMAGE] :
        a.result = str(a.action_value_1)
        a.duration = a.action_value_3
    # BUFF_DEBUFF
    elif a.action_type == ActionType.BUFF_DEBUFF:
        if a.action_value_1 == 1:
            a.result = str(a.action_value_2)
            a.duration = a.action_value_4
        elif a.action_value_1 == 2:
            a.result = "{}%".format(a.action_value_2)
            a.duration = a.action_value_4
    elif a.action_type in [90]:
        a.result = a.action_value_2
    elif a.action_type == ActionType.ACCUMULATIVE_DAMAGE:
        if a.action_value_1 == 1:
            value = a.action_value_2
        else: # a.action_value_1 == 2
            value = "{}%".format(a.action_value_2)
        a.result = "{}, count {}".format(value, int(a.action_value_4))
    elif a.action_type in [ActionType.BLIND, ActionType.CHARM]:
        a.result = "{}%".format(a.action_value_3)
    elif a.action_type == ActionType.KNOCK:
        a.result = a.action_value_1
    elif a.action_type == ActionType.DAMAGE_CHARGE:
        a.result = a.action_value_1
    elif a.action_type == ActionType.SUMMON:
        a.result = ""
    # REGENERATION
    elif a.action_type == ActionType.REGENERATION:
        a.duration = a.action_value_5
    # if a.action_type in self.skill_type_table:
    #     a.action_code = self.skill_type_table[a.action_type]