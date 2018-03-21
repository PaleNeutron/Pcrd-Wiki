# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ActualUnitBackground(models.Model):
    unit_id = models.IntegerField(primary_key=True)
    unit_name = models.TextField()
    bg_id = models.IntegerField()
    face_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'actual_unit_background'


class AilmentData(models.Model):
    ailment_id = models.IntegerField(primary_key=True)
    ailment_action = models.IntegerField()
    ailment_detail_1 = models.IntegerField()
    ailment_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'ailment_data'


class AlbumProductionList(models.Model):
    id = models.IntegerField(primary_key=True)
    unit_id = models.IntegerField()
    type = models.IntegerField()
    title = models.TextField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'album_production_list'


class AlbumVoiceList(models.Model):
    id = models.IntegerField(primary_key=True)
    unit_id = models.IntegerField()
    sheet_id = models.TextField()
    voice_id = models.TextField()
    title = models.TextField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'album_voice_list'


class ArenaDailyRankReward(models.Model):
    id = models.IntegerField(primary_key=True)
    rank_from = models.IntegerField()
    rank_to = models.IntegerField()
    reward_type_1 = models.IntegerField()
    reward_id_1 = models.IntegerField()
    reward_num_1 = models.IntegerField()
    reward_type_2 = models.IntegerField()
    reward_id_2 = models.IntegerField()
    reward_num_2 = models.IntegerField()
    reward_type_3 = models.IntegerField()
    reward_id_3 = models.IntegerField()
    reward_num_3 = models.IntegerField()
    reward_type_4 = models.IntegerField()
    reward_id_4 = models.IntegerField()
    reward_num_4 = models.IntegerField()
    reward_type_5 = models.IntegerField()
    reward_id_5 = models.IntegerField()
    reward_num_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'arena_daily_rank_reward'


class ArenaDefenceReward(models.Model):
    id = models.IntegerField(primary_key=True)
    limit_count = models.IntegerField()
    reward_type_1 = models.IntegerField()
    reward_id_1 = models.IntegerField()
    reward_num_1 = models.IntegerField()
    reward_type_2 = models.IntegerField()
    reward_id_2 = models.IntegerField()
    reward_num_2 = models.IntegerField()
    reward_type_3 = models.IntegerField()
    reward_id_3 = models.IntegerField()
    reward_num_3 = models.IntegerField()
    reward_type_4 = models.IntegerField()
    reward_id_4 = models.IntegerField()
    reward_num_4 = models.IntegerField()
    reward_type_5 = models.IntegerField()
    reward_id_5 = models.IntegerField()
    reward_num_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'arena_defence_reward'


class ArenaMaxRankReward(models.Model):
    id = models.IntegerField(primary_key=True)
    rank_from = models.IntegerField()
    rank_to = models.IntegerField()
    reward_type_1 = models.IntegerField()
    reward_id_1 = models.IntegerField()
    reward_num_1 = models.IntegerField()
    reward_type_2 = models.IntegerField()
    reward_id_2 = models.IntegerField()
    reward_num_2 = models.IntegerField()
    reward_type_3 = models.IntegerField()
    reward_id_3 = models.IntegerField()
    reward_num_3 = models.IntegerField()
    reward_type_4 = models.IntegerField()
    reward_id_4 = models.IntegerField()
    reward_num_4 = models.IntegerField()
    reward_type_5 = models.IntegerField()
    reward_id_5 = models.IntegerField()
    reward_num_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'arena_max_rank_reward'


class Banner(models.Model):
    banner_id = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    system_id = models.IntegerField()
    priority = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'banner'


class BgData(models.Model):
    view_name = models.TextField(unique=True)
    bg_id = models.IntegerField()
    event_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bg_data'


class CampaignSchedule(models.Model):
    id = models.IntegerField(primary_key=True)
    campaign_category = models.IntegerField()
    value = models.FloatField()
    system_id = models.IntegerField()
    icon_image = models.IntegerField()
    start_time = models.TextField()
    end_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'campaign_schedule'


class CharaStoryStatus(models.Model):
    story_id = models.IntegerField(primary_key=True)
    unlock_story_name = models.TextField()
    status_type_1 = models.IntegerField()
    status_rate_1 = models.IntegerField()
    status_type_2 = models.IntegerField()
    status_rate_2 = models.IntegerField()
    status_type_3 = models.IntegerField()
    status_rate_3 = models.IntegerField()
    status_type_4 = models.IntegerField()
    status_rate_4 = models.IntegerField()
    status_type_5 = models.IntegerField()
    status_rate_5 = models.IntegerField()
    chara_id_1 = models.IntegerField()
    chara_id_2 = models.IntegerField()
    chara_id_3 = models.IntegerField()
    chara_id_4 = models.IntegerField()
    chara_id_5 = models.IntegerField()
    chara_id_6 = models.IntegerField()
    chara_id_7 = models.IntegerField()
    chara_id_8 = models.IntegerField()
    chara_id_9 = models.IntegerField()
    chara_id_10 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chara_story_status'


class CharacterLoveRankupText(models.Model):
    chara_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    love_level = models.IntegerField()
    scale = models.FloatField()
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    voice_id_1 = models.IntegerField()
    face_1 = models.IntegerField()
    serif_1 = models.TextField()
    voice_id_2 = models.IntegerField()
    face_2 = models.IntegerField()
    serif_2 = models.TextField()
    voice_id_3 = models.IntegerField()
    face_3 = models.IntegerField()
    serif_3 = models.TextField()

    class Meta:
        managed = False
        db_table = 'character_love_rankup_text'


class ClanBattleBossDamageRank(models.Model):
    id = models.IntegerField(primary_key=True)
    damage_rank_id = models.IntegerField()
    ranking_from = models.IntegerField()
    ranking_to = models.IntegerField()
    odds_group_id = models.IntegerField()
    reward_type_1 = models.IntegerField()
    reward_id_1 = models.IntegerField()
    reward_num_1 = models.IntegerField()
    reward_type_2 = models.IntegerField()
    reward_id_2 = models.IntegerField()
    reward_num_2 = models.IntegerField()
    reward_type_3 = models.IntegerField()
    reward_id_3 = models.IntegerField()
    reward_num_3 = models.IntegerField()
    reward_type_4 = models.IntegerField()
    reward_id_4 = models.IntegerField()
    reward_num_4 = models.IntegerField()
    reward_type_5 = models.IntegerField()
    reward_id_5 = models.IntegerField()
    reward_num_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_battle_boss_damage_rank'
        unique_together = (('damage_rank_id', 'ranking_from', 'ranking_to'),)


class ClanBattleBossData(models.Model):
    boss_id = models.IntegerField(primary_key=True)
    clan_battle_id = models.IntegerField()
    difficulty = models.IntegerField()
    order_num = models.IntegerField()
    boss_thumb_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_battle_boss_data'


class ClanBattleBossFixReward(models.Model):
    fix_reward_id = models.IntegerField(primary_key=True)
    reward_type_1 = models.IntegerField()
    reward_id_1 = models.IntegerField()
    reward_num_1 = models.IntegerField()
    reward_type_2 = models.IntegerField()
    reward_id_2 = models.IntegerField()
    reward_num_2 = models.IntegerField()
    reward_type_3 = models.IntegerField()
    reward_id_3 = models.IntegerField()
    reward_num_3 = models.IntegerField()
    reward_type_4 = models.IntegerField()
    reward_id_4 = models.IntegerField()
    reward_num_4 = models.IntegerField()
    reward_type_5 = models.IntegerField()
    reward_id_5 = models.IntegerField()
    reward_num_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_battle_boss_fix_reward'


class ClanBattleBossGroup(models.Model):
    clan_battle_boss_group_id = models.IntegerField(primary_key=True)
    order_num = models.IntegerField()
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    limit_time = models.IntegerField()
    scale_ratio = models.FloatField()
    map_position_x = models.IntegerField()
    map_position_y = models.IntegerField()
    cursor_position = models.IntegerField()
    result_boss_position_y = models.IntegerField()
    chest_id = models.IntegerField()
    fix_reward_id = models.IntegerField()
    damage_rank_id = models.IntegerField()
    quest_detail_bg_id = models.IntegerField()
    quest_detail_bg_position = models.IntegerField()
    quest_detail_monster_size = models.FloatField()
    quest_detail_monster_height = models.IntegerField()
    battle_report_monster_size = models.FloatField()
    battle_report_monster_height = models.IntegerField()
    background = models.IntegerField()
    wave_group_id = models.IntegerField()
    reward_gold_coefficient = models.FloatField()
    limited_mana = models.IntegerField()
    wave_bgm = models.TextField()

    class Meta:
        managed = False
        db_table = 'clan_battle_boss_group'
        unique_together = (('clan_battle_boss_group_id', 'order_num'),)


class ClanBattleHpResetCost(models.Model):
    id = models.IntegerField(primary_key=True)
    reset_count_from = models.IntegerField()
    reset_count_to = models.IntegerField()
    cost_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_battle_hp_reset_cost'


class ClanBattleMapData(models.Model):
    id = models.IntegerField(primary_key=True)
    clan_battle_id = models.IntegerField()
    map_bg = models.IntegerField()
    difficulty = models.IntegerField()
    lap_num_from = models.IntegerField()
    lap_num_to = models.IntegerField()
    clan_battle_boss_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_battle_map_data'


class ClanBattleOddsData(models.Model):
    odds_group_id = models.IntegerField(primary_key=True)
    team_level_from = models.IntegerField()
    team_level_to = models.IntegerField()
    odds_csv_1 = models.TextField()
    odds_csv_2 = models.TextField()
    odds_csv_3 = models.TextField()
    odds_csv_4 = models.TextField()
    odds_csv_5 = models.TextField()
    odds_csv_6 = models.TextField()
    odds_csv_7 = models.TextField()
    odds_csv_8 = models.TextField()
    odds_csv_9 = models.TextField()
    odds_csv_10 = models.TextField()

    class Meta:
        managed = False
        db_table = 'clan_battle_odds_data'
        unique_together = (('odds_group_id', 'team_level_from', 'team_level_to'),)


class ClanBattlePeriod(models.Model):
    clan_battle_id = models.IntegerField(primary_key=True)
    period = models.IntegerField()
    period_detail = models.TextField()
    period_detail_bg = models.IntegerField()
    period_detail_bg_position = models.IntegerField()
    period_detail_boss_position_x = models.IntegerField()
    period_detail_boss_position_y = models.IntegerField()
    start_time = models.TextField()
    end_time = models.TextField()
    interval_start = models.TextField()
    interval_end = models.TextField()
    calc_start = models.TextField()
    result_start = models.TextField()
    result_end = models.TextField()

    class Meta:
        managed = False
        db_table = 'clan_battle_period'
        unique_together = (('clan_battle_id', 'period'),)


class ClanBattlePeriodRankBonus(models.Model):
    ranking_bonus_group_id = models.IntegerField(primary_key=True)
    rank_from = models.IntegerField()
    rank_to = models.IntegerField()
    reward_type_1 = models.IntegerField()
    reward_id_1 = models.IntegerField()
    reward_num_1 = models.IntegerField()
    reward_type_2 = models.IntegerField()
    reward_id_2 = models.IntegerField()
    reward_num_2 = models.IntegerField()
    reward_type_3 = models.IntegerField()
    reward_id_3 = models.IntegerField()
    reward_num_3 = models.IntegerField()
    reward_type_4 = models.IntegerField()
    reward_id_4 = models.IntegerField()
    reward_num_4 = models.IntegerField()
    reward_type_5 = models.IntegerField()
    reward_id_5 = models.IntegerField()
    reward_num_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_battle_period_rank_bonus'
        unique_together = (('ranking_bonus_group_id', 'rank_from', 'rank_to'),)


class ClanBattlePeriodRankReward(models.Model):
    id = models.IntegerField(primary_key=True)
    clan_battle_id = models.IntegerField()
    period = models.IntegerField()
    rank_from = models.IntegerField()
    rank_to = models.IntegerField()
    ranking_bonus_group = models.IntegerField()
    reward_type_1 = models.IntegerField()
    reward_id_1 = models.IntegerField()
    reward_num_1 = models.IntegerField()
    reward_type_2 = models.IntegerField()
    reward_id_2 = models.IntegerField()
    reward_num_2 = models.IntegerField()
    reward_type_3 = models.IntegerField()
    reward_id_3 = models.IntegerField()
    reward_num_3 = models.IntegerField()
    reward_type_4 = models.IntegerField()
    reward_id_4 = models.IntegerField()
    reward_num_4 = models.IntegerField()
    reward_type_5 = models.IntegerField()
    reward_id_5 = models.IntegerField()
    reward_num_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_battle_period_rank_reward'


class ClanBattleSchedule(models.Model):
    clan_battle_id = models.IntegerField(primary_key=True)
    release_month = models.IntegerField()
    last_clan_battle_id = models.IntegerField()
    point_per_stamina = models.IntegerField()
    cost_group_id = models.IntegerField()
    map_bgm = models.TextField()
    resource_id = models.IntegerField()
    start_time = models.TextField()
    end_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'clan_battle_schedule'


class ClanBattleTotalRank(models.Model):
    id = models.IntegerField(primary_key=True)
    clan_battle_id = models.IntegerField()
    rank_from = models.IntegerField()
    rank_to = models.IntegerField()
    reward_type_1 = models.IntegerField()
    reward_id_1 = models.IntegerField()
    reward_num_1 = models.IntegerField()
    reward_type_2 = models.IntegerField()
    reward_id_2 = models.IntegerField()
    reward_num_2 = models.IntegerField()
    reward_type_3 = models.IntegerField()
    reward_id_3 = models.IntegerField()
    reward_num_3 = models.IntegerField()
    reward_type_4 = models.IntegerField()
    reward_id_4 = models.IntegerField()
    reward_num_4 = models.IntegerField()
    reward_type_5 = models.IntegerField()
    reward_id_5 = models.IntegerField()
    reward_num_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_battle_total_rank'


class ClanCostGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    cost_group_id = models.IntegerField()
    difficulty = models.IntegerField()
    count = models.IntegerField()
    cost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_cost_group'


class ClanGrade(models.Model):
    clan_grade_id = models.IntegerField(primary_key=True)
    rank_from = models.IntegerField()
    rank_to = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_grade'


class ClanInviteLevelGroup(models.Model):
    level_group_id = models.IntegerField(primary_key=True)
    team_level_from = models.IntegerField()
    team_level_to = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_invite_level_group'


class ContentReleaseData(models.Model):
    system_id = models.IntegerField(primary_key=True)
    team_level = models.IntegerField()
    story_id = models.IntegerField()
    quest_id = models.IntegerField()
    dialog = models.TextField()

    class Meta:
        managed = False
        db_table = 'content_release_data'


class CooperationQuestData(models.Model):
    quest_id = models.IntegerField(primary_key=True)
    quest_name = models.TextField()
    difficulty_level = models.IntegerField()
    limit_team_level = models.IntegerField()
    team_exp = models.IntegerField()
    exp = models.IntegerField()
    limit_time = models.IntegerField()
    clear_reward_group_id = models.IntegerField()
    odds_group_id = models.IntegerField()
    lobby_background = models.IntegerField()
    background_1 = models.IntegerField()
    wave_group_id_1 = models.IntegerField()
    wave_bgm_sheet_id_1 = models.TextField()
    wave_bgm_que_id_1 = models.TextField()
    background_2 = models.IntegerField()
    wave_group_id_2 = models.IntegerField()
    wave_bgm_sheet_id_2 = models.TextField()
    wave_bgm_que_id_2 = models.TextField()
    background_3 = models.IntegerField()
    wave_group_id_3 = models.IntegerField()
    wave_bgm_sheet_id_3 = models.TextField()
    wave_bgm_que_id_3 = models.TextField()
    enemy_image_1 = models.IntegerField()
    enemy_image_2 = models.IntegerField()
    enemy_image_3 = models.IntegerField()
    enemy_image_4 = models.IntegerField()
    enemy_image_5 = models.IntegerField()
    first_reward_image_1 = models.IntegerField()
    first_reward_image_2 = models.IntegerField()
    first_reward_image_3 = models.IntegerField()
    first_reward_image_4 = models.IntegerField()
    first_reward_image_5 = models.IntegerField()
    repeat_reward_image_1 = models.IntegerField()
    repeat_reward_image_2 = models.IntegerField()
    repeat_reward_image_3 = models.IntegerField()
    cooperation_quest_detail_bg_id = models.IntegerField()
    cooperation_quest_detail_bg_position = models.IntegerField()
    main_enemy_image_wave_1 = models.IntegerField()
    sub_enemy_image_wave_1_1 = models.IntegerField()
    sub_enemy_image_wave_1_2 = models.IntegerField()
    sub_enemy_image_wave_1_3 = models.IntegerField()
    sub_enemy_image_wave_1_4 = models.IntegerField()
    main_enemy_image_wave_2 = models.IntegerField()
    sub_enemy_image_wave_2_1 = models.IntegerField()
    sub_enemy_image_wave_2_2 = models.IntegerField()
    sub_enemy_image_wave_2_3 = models.IntegerField()
    sub_enemy_image_wave_2_4 = models.IntegerField()
    main_enemy_image_wave_3 = models.IntegerField()
    sub_enemy_image_wave_3_1 = models.IntegerField()
    sub_enemy_image_wave_3_2 = models.IntegerField()
    sub_enemy_image_wave_3_3 = models.IntegerField()
    sub_enemy_image_wave_3_4 = models.IntegerField()
    quest_comment = models.TextField()
    unlock_quest_id_1 = models.IntegerField()
    unlock_quest_id_2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cooperation_quest_data'


class DailyMissionData(models.Model):
    daily_mission_id = models.IntegerField(primary_key=True)
    disp_group = models.IntegerField()
    category_icon = models.IntegerField()
    description = models.TextField()
    mission_condition = models.IntegerField()
    condition_value_1 = models.IntegerField(blank=True, null=True)
    condition_value_2 = models.IntegerField(blank=True, null=True)
    condition_value_3 = models.IntegerField(blank=True, null=True)
    condition_num = models.IntegerField()
    mission_reward_id = models.IntegerField()
    system_id = models.IntegerField(blank=True, null=True)
    start_time = models.TextField()
    end_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'daily_mission_data'


class DungeonAreaData(models.Model):
    dungeon_area_id = models.IntegerField(primary_key=True)
    dungeon_type = models.IntegerField()
    dungeon_name = models.TextField()
    description = models.TextField()
    open_quest_id = models.IntegerField()
    content_release_story = models.IntegerField()
    initial_clear_story = models.IntegerField()
    wave_group_id = models.IntegerField()
    reward_group_id = models.IntegerField()
    recommend_level = models.IntegerField()
    quest_position_x = models.IntegerField()
    quest_position_y = models.IntegerField()
    icon_id = models.IntegerField()
    coin_item_id = models.IntegerField()
    enemy_image_1 = models.IntegerField()
    enemy_image_2 = models.IntegerField()
    enemy_image_3 = models.IntegerField()
    enemy_image_4 = models.IntegerField()
    enemy_image_5 = models.IntegerField()
    view_reward_id_1 = models.IntegerField()
    view_reward_id_2 = models.IntegerField()
    view_reward_id_3 = models.IntegerField()
    view_reward_id_4 = models.IntegerField()
    view_reward_id_5 = models.IntegerField()
    recovery_hp_rate = models.IntegerField()
    recovery_tp_rate = models.IntegerField()
    start_time = models.TextField()
    end_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'dungeon_area_data'


class DungeonQuestData(models.Model):
    quest_id = models.IntegerField(primary_key=True)
    dungeon_area_id = models.IntegerField()
    floor_num = models.IntegerField()
    limit_time = models.IntegerField()
    matching_coefficient = models.FloatField()
    reward_image_1 = models.IntegerField()
    reward_image_2 = models.IntegerField()
    reward_image_3 = models.IntegerField()
    reward_coin = models.IntegerField()
    chest_id = models.IntegerField()
    odds_group_id = models.IntegerField()
    background = models.IntegerField()
    dungeon_quest_detail_bg_id = models.IntegerField()
    dungeon_quest_detail_bg_position = models.IntegerField()
    dungeon_quest_detail_monster_size = models.FloatField()
    dungeon_quest_detail_monster_height = models.FloatField()
    wave_bgm_sheet_id_1 = models.TextField()
    wave_bgm_que_id_1 = models.TextField()

    class Meta:
        managed = False
        db_table = 'dungeon_quest_data'


class EnemyParameter(models.Model):
    enemy_id = models.IntegerField(primary_key=True)
    unit_id = models.IntegerField()
    name = models.TextField()
    level = models.IntegerField()
    rarity = models.IntegerField()
    promotion_level = models.IntegerField()
    hp = models.IntegerField()
    atk = models.IntegerField()
    magic_str = models.IntegerField()
    def_field = models.IntegerField(db_column='def')  # Field renamed because it was a Python reserved word.
    magic_def = models.IntegerField()
    physical_critical = models.IntegerField()
    magic_critical = models.IntegerField()
    wave_hp_recovery = models.IntegerField()
    wave_energy_recovery = models.IntegerField()
    dodge = models.IntegerField()
    physical_penetrate = models.IntegerField()
    magic_penetrate = models.IntegerField()
    life_steal = models.IntegerField()
    hp_recovery_rate = models.IntegerField()
    energy_recovery_rate = models.IntegerField()
    energy_reduce_rate = models.IntegerField()
    union_burst_level = models.IntegerField()
    main_skill_lv_1 = models.IntegerField()
    main_skill_lv_2 = models.IntegerField()
    main_skill_lv_3 = models.IntegerField()
    main_skill_lv_4 = models.IntegerField()
    main_skill_lv_5 = models.IntegerField()
    main_skill_lv_6 = models.IntegerField()
    main_skill_lv_7 = models.IntegerField()
    main_skill_lv_8 = models.IntegerField()
    main_skill_lv_9 = models.IntegerField()
    main_skill_lv_10 = models.IntegerField()
    ex_skill_lv_1 = models.IntegerField()
    ex_skill_lv_2 = models.IntegerField()
    ex_skill_lv_3 = models.IntegerField()
    ex_skill_lv_4 = models.IntegerField()
    ex_skill_lv_5 = models.IntegerField()
    resist_status_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'enemy_parameter'


class EnemyRewardData(models.Model):
    drop_reward_id = models.IntegerField(primary_key=True)
    drop_count = models.IntegerField()
    reward_type_1 = models.IntegerField()
    reward_id_1 = models.IntegerField()
    reward_num_1 = models.IntegerField()
    odds_1 = models.IntegerField()
    reward_type_2 = models.IntegerField()
    reward_id_2 = models.IntegerField()
    reward_num_2 = models.IntegerField()
    odds_2 = models.IntegerField()
    reward_type_3 = models.IntegerField()
    reward_id_3 = models.IntegerField()
    reward_num_3 = models.IntegerField()
    odds_3 = models.IntegerField()
    reward_type_4 = models.IntegerField()
    reward_id_4 = models.IntegerField()
    reward_num_4 = models.IntegerField()
    odds_4 = models.IntegerField()
    reward_type_5 = models.IntegerField()
    reward_id_5 = models.IntegerField()
    reward_num_5 = models.IntegerField()
    odds_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'enemy_reward_data'


class EquipmentCraft(models.Model):
    equipment_id = models.IntegerField(primary_key=True)
    crafted_cost = models.IntegerField()
    condition_equipment_id_1 = models.IntegerField()
    consume_num_1 = models.IntegerField()
    condition_equipment_id_2 = models.IntegerField()
    consume_num_2 = models.IntegerField()
    condition_equipment_id_3 = models.IntegerField()
    consume_num_3 = models.IntegerField()
    condition_equipment_id_4 = models.IntegerField()
    consume_num_4 = models.IntegerField()
    condition_equipment_id_5 = models.IntegerField()
    consume_num_5 = models.IntegerField()
    condition_equipment_id_6 = models.IntegerField()
    consume_num_6 = models.IntegerField()
    condition_equipment_id_7 = models.IntegerField()
    consume_num_7 = models.IntegerField()
    condition_equipment_id_8 = models.IntegerField()
    consume_num_8 = models.IntegerField()
    condition_equipment_id_9 = models.IntegerField()
    consume_num_9 = models.IntegerField()
    condition_equipment_id_10 = models.IntegerField()
    consume_num_10 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'equipment_craft'


class EquipmentData(models.Model):
    equipment_id = models.IntegerField(primary_key=True)
    equipment_name = models.TextField()
    description = models.TextField()
    promotion_level = models.IntegerField()
    craft_flg = models.IntegerField()
    equipment_enhance_point = models.IntegerField()
    sale_price = models.IntegerField()
    require_level = models.IntegerField()
    hp = models.FloatField()
    atk = models.FloatField()
    magic_str = models.FloatField()
    def_field = models.FloatField(db_column='def')  # Field renamed because it was a Python reserved word.
    magic_def = models.FloatField()
    physical_critical = models.FloatField()
    magic_critical = models.FloatField()
    wave_hp_recovery = models.FloatField()
    wave_energy_recovery = models.FloatField()
    dodge = models.FloatField()
    physical_penetrate = models.FloatField()
    magic_penetrate = models.FloatField()
    life_steal = models.FloatField()
    hp_recovery_rate = models.FloatField()
    energy_recovery_rate = models.FloatField()
    energy_reduce_rate = models.FloatField()
    enable_donation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'equipment_data'


class EquipmentDonation(models.Model):
    team_level = models.IntegerField()
    donation_num_once = models.IntegerField()
    donation_num_daily = models.IntegerField()
    request_num_once = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'equipment_donation'


class EquipmentEnhanceData(models.Model):
    promotion_level = models.IntegerField()
    equipment_enhance_level = models.IntegerField()
    needed_point = models.IntegerField()
    total_point = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'equipment_enhance_data'
        unique_together = (('promotion_level', 'equipment_enhance_level'),)


class EquipmentEnhanceRate(models.Model):
    equipment_id = models.IntegerField(primary_key=True)
    equipment_name = models.TextField()
    description = models.TextField()
    promotion_level = models.IntegerField()
    hp = models.FloatField()
    atk = models.FloatField()
    magic_str = models.FloatField()
    def_field = models.FloatField(db_column='def')  # Field renamed because it was a Python reserved word.
    magic_def = models.FloatField()
    physical_critical = models.FloatField()
    magic_critical = models.FloatField()
    wave_hp_recovery = models.FloatField()
    wave_energy_recovery = models.FloatField()
    dodge = models.FloatField()
    physical_penetrate = models.FloatField()
    magic_penetrate = models.FloatField()
    life_steal = models.FloatField()
    hp_recovery_rate = models.FloatField()
    energy_recovery_rate = models.FloatField()
    energy_reduce_rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'equipment_enhance_rate'


class EventBgData(models.Model):
    event_id = models.IntegerField(primary_key=True)
    bg_id = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'event_bg_data'


class EventStoryData(models.Model):
    story_group_id = models.IntegerField(primary_key=True)
    story_type = models.IntegerField()
    value = models.IntegerField()
    title = models.TextField()
    thumbnail_id = models.IntegerField()
    disp_order = models.IntegerField()
    start_time = models.TextField()
    end_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'event_story_data'


class ExperienceTeam(models.Model):
    team_level = models.IntegerField()
    total_exp = models.IntegerField()
    max_stamina = models.IntegerField()
    over_limit_stamina = models.IntegerField()
    recover_stamina_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'experience_team'


class ExperienceUnit(models.Model):
    unit_level = models.IntegerField()
    total_exp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'experience_unit'


class GachaData(models.Model):
    gacha_id = models.IntegerField(primary_key=True)
    gacha_name = models.TextField()
    description = models.TextField()
    gacha_detail = models.IntegerField()
    gacha_cost_type = models.IntegerField()
    price = models.IntegerField()
    free_gacha_type = models.IntegerField()
    free_gacha_interval_time = models.IntegerField()
    free_gacha_count = models.IntegerField()
    discount_price = models.IntegerField()
    gacha_odds = models.TextField()
    gacha_odds_star2 = models.TextField()
    gacha_type = models.IntegerField()
    movie_id = models.IntegerField()
    start_time = models.TextField()
    end_time = models.TextField()
    ticket_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacha_data'


class GiftMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    discription = models.TextField()
    type_1 = models.IntegerField()
    type_2 = models.IntegerField()
    type_3 = models.IntegerField()
    type_4 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gift_message'


class GoldsetData(models.Model):
    id = models.IntegerField(primary_key=True)
    buy_count = models.IntegerField()
    use_jewel_count = models.IntegerField()
    get_gold_count = models.IntegerField()
    goldset_odds_1 = models.IntegerField()
    goldset_odds_2 = models.IntegerField()
    goldset_odds_3 = models.IntegerField()
    additional_gold_min_rate = models.IntegerField()
    additional_gold_max_rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'goldset_data'


class GoldsetDataTeamlevel(models.Model):
    id = models.IntegerField(primary_key=True)
    team_level = models.IntegerField()
    initial_get_gold_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'goldset_data_teamlevel'


class GrandArenaDailyRankReward(models.Model):
    id = models.IntegerField(primary_key=True)
    rank_from = models.IntegerField()
    rank_to = models.IntegerField()
    reward_type_1 = models.IntegerField()
    reward_id_1 = models.IntegerField()
    reward_num_1 = models.IntegerField()
    reward_type_2 = models.IntegerField()
    reward_id_2 = models.IntegerField()
    reward_num_2 = models.IntegerField()
    reward_type_3 = models.IntegerField()
    reward_id_3 = models.IntegerField()
    reward_num_3 = models.IntegerField()
    reward_type_4 = models.IntegerField()
    reward_id_4 = models.IntegerField()
    reward_num_4 = models.IntegerField()
    reward_type_5 = models.IntegerField()
    reward_id_5 = models.IntegerField()
    reward_num_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'grand_arena_daily_rank_reward'


class GrandArenaDefenceReward(models.Model):
    id = models.IntegerField(primary_key=True)
    limit_count = models.IntegerField()
    reward_type_1 = models.IntegerField()
    reward_id_1 = models.IntegerField()
    reward_num_1 = models.IntegerField()
    reward_type_2 = models.IntegerField()
    reward_id_2 = models.IntegerField()
    reward_num_2 = models.IntegerField()
    reward_type_3 = models.IntegerField()
    reward_id_3 = models.IntegerField()
    reward_num_3 = models.IntegerField()
    reward_type_4 = models.IntegerField()
    reward_id_4 = models.IntegerField()
    reward_num_4 = models.IntegerField()
    reward_type_5 = models.IntegerField()
    reward_id_5 = models.IntegerField()
    reward_num_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'grand_arena_defence_reward'


class GrandArenaMaxRankReward(models.Model):
    id = models.IntegerField(primary_key=True)
    rank_from = models.IntegerField()
    rank_to = models.IntegerField()
    reward_type_1 = models.IntegerField()
    reward_id_1 = models.IntegerField()
    reward_num_1 = models.IntegerField()
    reward_type_2 = models.IntegerField()
    reward_id_2 = models.IntegerField()
    reward_num_2 = models.IntegerField()
    reward_type_3 = models.IntegerField()
    reward_id_3 = models.IntegerField()
    reward_num_3 = models.IntegerField()
    reward_type_4 = models.IntegerField()
    reward_id_4 = models.IntegerField()
    reward_num_4 = models.IntegerField()
    reward_type_5 = models.IntegerField()
    reward_id_5 = models.IntegerField()
    reward_num_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'grand_arena_max_rank_reward'


class Guild(models.Model):
    guild_id = models.IntegerField(primary_key=True)
    guild_name = models.TextField()
    description = models.TextField()
    guild_master = models.IntegerField()
    member1 = models.IntegerField()
    member2 = models.IntegerField()
    member3 = models.IntegerField()
    member4 = models.IntegerField()
    member5 = models.IntegerField()
    member6 = models.IntegerField()
    member7 = models.IntegerField()
    member8 = models.IntegerField()
    member9 = models.IntegerField()
    member10 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'guild'


class ItemData(models.Model):
    item_id = models.IntegerField(primary_key=True)
    item_name = models.TextField()
    description = models.TextField()
    promotion_level = models.IntegerField()
    item_type = models.IntegerField()
    value = models.IntegerField()
    price = models.IntegerField()
    limit_num = models.IntegerField()
    start_time = models.TextField()
    end_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'item_data'


class Lipsync(models.Model):
    voice_id = models.TextField(unique=True)
    time = models.TextField()
    is_enable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lipsync'


class LoginBonusData(models.Model):
    login_bonus_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    login_bonus_type = models.IntegerField()
    count_num = models.IntegerField()
    start_time = models.TextField()
    end_time = models.TextField()
    bg_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login_bonus_data'


class LoginBonusDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    login_bonus_id = models.IntegerField()
    count = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login_bonus_detail'


class LoveChara(models.Model):
    love_level = models.IntegerField()
    total_love = models.IntegerField()
    unlocked_class = models.IntegerField()
    rarity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'love_chara'


class MissionRewardData(models.Model):
    id = models.IntegerField(primary_key=True)
    mission_reward_id = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField(blank=True, null=True)
    reward_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mission_reward_data'


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    story_group_id = models.IntegerField()
    story_id = models.IntegerField()
    bgm_id = models.TextField()
    se_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'movie'


class NaviComment(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    where_type = models.IntegerField()
    character_id = models.IntegerField()
    face_type = models.IntegerField()
    character_name = models.TextField()
    description = models.TextField(blank=True, null=True)
    voice_id = models.IntegerField()
    start_time = models.TextField()
    end_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'navi_comment'


class PositionSetting(models.Model):
    position_setting_id = models.IntegerField(primary_key=True)
    front = models.IntegerField()
    middle = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'position_setting'


class QuestAreaData(models.Model):
    area_id = models.IntegerField(primary_key=True)
    area_name = models.TextField()
    map_type = models.IntegerField()
    sheet_id = models.TextField()
    que_id = models.TextField()
    start_time = models.TextField()
    end_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'quest_area_data'


class QuestConditionData(models.Model):
    quest_id = models.IntegerField(primary_key=True)
    condition_quest_id_1 = models.IntegerField()
    condition_quest_id_2 = models.IntegerField()
    condition_quest_id_3 = models.IntegerField()
    condition_quest_id_4 = models.IntegerField()
    condition_quest_id_5 = models.IntegerField()
    release_quest_id_1 = models.IntegerField()
    release_quest_id_2 = models.IntegerField()
    release_quest_id_3 = models.IntegerField()
    release_quest_id_4 = models.IntegerField()
    release_quest_id_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'quest_condition_data'


class QuestData(models.Model):
    quest_id = models.IntegerField(primary_key=True)
    area_id = models.IntegerField()
    quest_name = models.TextField()
    limit_team_level = models.IntegerField()
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    icon_id = models.IntegerField()
    stamina = models.IntegerField()
    stamina_start = models.IntegerField()
    team_exp = models.IntegerField()
    unit_exp = models.IntegerField()
    love = models.IntegerField()
    limit_time = models.IntegerField()
    daily_limit = models.IntegerField()
    clear_reward_group = models.IntegerField()
    rank_reward_group = models.IntegerField()
    background_1 = models.IntegerField()
    wave_group_id_1 = models.IntegerField()
    wave_bgm_sheet_id_1 = models.TextField()
    wave_bgm_que_id_1 = models.TextField()
    story_id_wavestart_1 = models.IntegerField()
    story_id_waveend_1 = models.IntegerField()
    background_2 = models.IntegerField()
    wave_group_id_2 = models.IntegerField()
    wave_bgm_sheet_id_2 = models.TextField()
    wave_bgm_que_id_2 = models.TextField()
    story_id_wavestart_2 = models.IntegerField()
    story_id_waveend_2 = models.IntegerField()
    background_3 = models.IntegerField()
    wave_group_id_3 = models.IntegerField()
    wave_bgm_sheet_id_3 = models.TextField()
    wave_bgm_que_id_3 = models.TextField()
    story_id_wavestart_3 = models.IntegerField()
    story_id_waveend_3 = models.IntegerField()
    enemy_image_1 = models.IntegerField()
    enemy_image_2 = models.IntegerField()
    enemy_image_3 = models.IntegerField()
    enemy_image_4 = models.IntegerField()
    enemy_image_5 = models.IntegerField()
    reward_image_1 = models.IntegerField()
    reward_image_2 = models.IntegerField()
    reward_image_3 = models.IntegerField()
    reward_image_4 = models.IntegerField()
    reward_image_5 = models.IntegerField()
    quest_detail_bg_id = models.IntegerField()
    quest_detail_bg_position = models.IntegerField()
    start_time = models.TextField()
    end_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'quest_data'


class QuestDefeatNotice(models.Model):
    id = models.IntegerField(primary_key=True)
    image_id = models.IntegerField()
    required_team_level = models.IntegerField()
    required_quest_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'quest_defeat_notice'


class QuestRewardData(models.Model):
    reward_group_id = models.IntegerField(primary_key=True)
    reward_type_1 = models.IntegerField()
    reward_id_1 = models.IntegerField()
    reward_num_1 = models.IntegerField()
    reward_type_2 = models.IntegerField()
    reward_id_2 = models.IntegerField()
    reward_num_2 = models.IntegerField()
    reward_type_3 = models.IntegerField()
    reward_id_3 = models.IntegerField()
    reward_num_3 = models.IntegerField()
    reward_type_4 = models.IntegerField()
    reward_id_4 = models.IntegerField()
    reward_num_4 = models.IntegerField()
    reward_type_5 = models.IntegerField()
    reward_id_5 = models.IntegerField()
    reward_num_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'quest_reward_data'


class ResistData(models.Model):
    resist_status_id = models.IntegerField(primary_key=True)
    ailment_1 = models.IntegerField()
    ailment_2 = models.IntegerField()
    ailment_3 = models.IntegerField()
    ailment_4 = models.IntegerField()
    ailment_5 = models.IntegerField()
    ailment_6 = models.IntegerField()
    ailment_7 = models.IntegerField()
    ailment_8 = models.IntegerField()
    ailment_9 = models.IntegerField()
    ailment_10 = models.IntegerField()
    ailment_11 = models.IntegerField()
    ailment_12 = models.IntegerField()
    ailment_13 = models.IntegerField()
    ailment_14 = models.IntegerField()
    ailment_15 = models.IntegerField()
    ailment_16 = models.IntegerField()
    ailment_17 = models.IntegerField()
    ailment_18 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'resist_data'


class RewardCollectGuide(models.Model):
    object_id = models.IntegerField(primary_key=True)
    quest_id_1 = models.IntegerField()
    quest_id_2 = models.IntegerField()
    quest_id_3 = models.IntegerField()
    quest_id_4 = models.IntegerField()
    quest_id_5 = models.IntegerField()
    quest_id_6 = models.IntegerField()
    quest_id_7 = models.IntegerField()
    quest_id_8 = models.IntegerField()
    quest_id_9 = models.IntegerField()
    quest_id_10 = models.IntegerField()
    system_id_1 = models.IntegerField()
    system_id_2 = models.IntegerField()
    system_id_3 = models.IntegerField()
    system_id_4 = models.IntegerField()
    system_id_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reward_collect_guide'


class RoomChange(models.Model):
    room_item_id = models.IntegerField(primary_key=True)
    change_id = models.IntegerField()
    change_start = models.TextField()
    change_end = models.TextField()

    class Meta:
        managed = False
        db_table = 'room_change'


class RoomCharacterPersonality(models.Model):
    character_id = models.IntegerField(primary_key=True)
    personality_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_character_personality'


class RoomChatFormation(models.Model):
    id = models.IntegerField(primary_key=True)
    unit_1_x = models.IntegerField()
    unit_1_y = models.IntegerField()
    unit_1_dir = models.IntegerField()
    unit_2_x = models.IntegerField()
    unit_2_y = models.IntegerField()
    unit_2_dir = models.IntegerField()
    unit_3_x = models.IntegerField(blank=True, null=True)
    unit_3_y = models.IntegerField(blank=True, null=True)
    unit_3_dir = models.IntegerField(blank=True, null=True)
    unit_4_x = models.IntegerField(blank=True, null=True)
    unit_4_y = models.IntegerField(blank=True, null=True)
    unit_4_dir = models.IntegerField(blank=True, null=True)
    unit_5_x = models.IntegerField(blank=True, null=True)
    unit_5_y = models.IntegerField(blank=True, null=True)
    unit_5_dir = models.IntegerField(blank=True, null=True)
    unit_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_chat_formation'


class RoomChatInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    formation_id = models.IntegerField()
    scenario_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_chat_info'


class RoomChatScenario(models.Model):
    id = models.IntegerField(primary_key=True)
    scenario_idx = models.IntegerField()
    unit_pos_no = models.IntegerField()
    delay = models.IntegerField()
    affect_type = models.IntegerField()
    anime_id = models.IntegerField()
    icon_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_chat_scenario'
        unique_together = (('id', 'scenario_idx'),)


class RoomEffect(models.Model):
    id = models.IntegerField(primary_key=True)
    reward_get = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_effect'


class RoomEffectRewardGet(models.Model):
    id = models.IntegerField(primary_key=True)
    level = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    max_count = models.IntegerField()
    inc_step = models.IntegerField()
    interval_second = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_effect_reward_get'
        unique_together = (('id', 'level'),)


class RoomEmotionIcon(models.Model):
    id = models.IntegerField(primary_key=True)
    enable_auto = models.IntegerField()
    enable_tap = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_emotion_icon'


class RoomItem(models.Model):
    id = models.IntegerField(primary_key=True)
    item_type = models.IntegerField()
    category = models.IntegerField()
    name = models.TextField()
    max_level = models.IntegerField()
    enable_remove = models.IntegerField()
    max_possession_num = models.IntegerField()
    effect_id_1 = models.IntegerField()
    shop_start = models.TextField()
    shop_end = models.TextField()
    shop_new_disp_end = models.TextField()
    cost_item_num = models.IntegerField()
    shop_open_type = models.IntegerField()
    shop_open_id = models.IntegerField()
    shop_open_value = models.IntegerField()
    sold_price = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_item'


class RoomItemAnnouncement(models.Model):
    id = models.IntegerField(primary_key=True)
    announcement_start = models.TextField()
    announcement_end = models.TextField()

    class Meta:
        managed = False
        db_table = 'room_item_announcement'


class RoomItemDetail(models.Model):
    room_item_id = models.IntegerField(primary_key=True)
    level = models.IntegerField()
    item_detail = models.TextField()
    lvup_trigger_type = models.IntegerField()
    lvup_trigger_id = models.IntegerField()
    lvup_trigger_value = models.IntegerField()
    lvup_item1_type = models.IntegerField()
    lvup_item1_id = models.IntegerField()
    lvup_item1_num = models.IntegerField()
    lvup_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_item_detail'
        unique_together = (('room_item_id', 'level'),)


class RoomReleaseData(models.Model):
    system_id = models.IntegerField(primary_key=True)
    story_id = models.IntegerField()
    pre_story_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_release_data'


class RoomSetup(models.Model):
    room_item_id = models.IntegerField(primary_key=True)
    grid_height = models.IntegerField()
    grid_width = models.IntegerField()
    unit_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_setup'


class RoomUnitComments(models.Model):
    id = models.IntegerField(primary_key=True)
    unit_id = models.IntegerField()
    trigger = models.IntegerField()
    voice_id = models.IntegerField()
    beloved_step = models.IntegerField()
    time = models.IntegerField()
    face_id = models.IntegerField()
    description = models.TextField()
    insert_word_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_unit_comments'
        unique_together = (('unit_id', 'trigger', 'voice_id', 'time'),)


class SeasonPack(models.Model):
    id = models.IntegerField(primary_key=True)
    mission_id = models.IntegerField()
    disp_order = models.IntegerField()
    category_icon = models.IntegerField()
    receive_text = models.TextField()
    after_text = models.TextField()
    term = models.IntegerField()
    repurchase_day = models.IntegerField()
    system_id_1 = models.IntegerField()
    add_num_1 = models.IntegerField()
    item_record_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'season_pack'


class ShopStaticPriceGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    price_group_id = models.IntegerField()
    buy_count_from = models.IntegerField()
    buy_count_to = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_static_price_group'


class SkillAction(models.Model):
    action_id = models.IntegerField(primary_key=True)
    class_id = models.IntegerField()
    action_type = models.IntegerField()
    action_detail_1 = models.IntegerField()
    action_detail_2 = models.IntegerField()
    action_detail_3 = models.IntegerField()
    action_value_1 = models.FloatField()
    action_value_2 = models.FloatField()
    action_value_3 = models.FloatField()
    action_value_4 = models.FloatField()
    action_value_5 = models.FloatField()
    action_value_6 = models.FloatField()
    action_value_7 = models.FloatField()
    target_assignment = models.IntegerField()
    target_area = models.IntegerField()
    target_range = models.IntegerField()
    target_type = models.IntegerField()
    target_number = models.IntegerField()
    target_count = models.IntegerField()
    description = models.TextField()
    level_up_disp = models.TextField()

    class Meta:
        managed = False
        db_table = 'skill_action'


class SkillCost(models.Model):
    target_level = models.IntegerField()
    cost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skill_cost'


class SkillData(models.Model):
    skill_id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    skill_type = models.IntegerField()
    skill_area_width = models.IntegerField()
    skill_cast_time = models.FloatField()
    action_1 = models.IntegerField()
    action_2 = models.IntegerField()
    action_3 = models.IntegerField()
    action_4 = models.IntegerField()
    action_5 = models.IntegerField()
    action_6 = models.IntegerField()
    action_7 = models.IntegerField()
    depend_action_1 = models.IntegerField()
    depend_action_2 = models.IntegerField()
    depend_action_3 = models.IntegerField()
    depend_action_4 = models.IntegerField()
    depend_action_5 = models.IntegerField()
    depend_action_6 = models.IntegerField()
    depend_action_7 = models.IntegerField()
    description = models.TextField()
    icon_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skill_data'


class SkipMonsterData(models.Model):
    quest_id = models.IntegerField(primary_key=True)
    area_id = models.IntegerField()
    quest_name = models.TextField()
    wave_group_id_1 = models.IntegerField()
    bg_skip_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skip_monster_data'


class SqliteStat1(models.Model):
    tbl = models.TextField(blank=True, null=True)  # This field type is a guess.
    idx = models.TextField(blank=True, null=True)  # This field type is a guess.
    stat = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sqlite_stat1'


class Stamp(models.Model):
    stamp_id = models.IntegerField(primary_key=True)
    disp_order = models.IntegerField()
    description = models.TextField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'stamp'


class StationaryMissionData(models.Model):
    stationary_mission_id = models.IntegerField(primary_key=True)
    disp_group = models.IntegerField()
    category_icon = models.IntegerField()
    description = models.TextField()
    mission_condition = models.IntegerField()
    condition_value_1 = models.IntegerField(blank=True, null=True)
    condition_value_2 = models.IntegerField(blank=True, null=True)
    condition_value_3 = models.IntegerField(blank=True, null=True)
    condition_num = models.IntegerField()
    mission_reward_id = models.IntegerField()
    system_id = models.IntegerField(blank=True, null=True)
    start_time = models.TextField()
    end_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'stationary_mission_data'


class Still(models.Model):
    still_id = models.IntegerField(primary_key=True)
    story_group_id = models.IntegerField()
    story_id = models.IntegerField()
    still_group_id = models.IntegerField()
    vertical_still_flg = models.IntegerField()
    position_y = models.IntegerField()
    unit_id_1 = models.IntegerField()
    unit_id_2 = models.IntegerField()
    unit_id_3 = models.IntegerField()
    unit_id_4 = models.IntegerField()
    unit_id_5 = models.IntegerField()
    unit_id_6 = models.IntegerField()
    unit_id_7 = models.IntegerField()
    unit_id_8 = models.IntegerField()
    unit_id_9 = models.IntegerField()
    unit_id_10 = models.IntegerField()
    facial_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'still'


class StoryCharacterMask(models.Model):
    chara_id = models.IntegerField(primary_key=True)
    offset = models.FloatField()
    size = models.FloatField()
    softness = models.FloatField()

    class Meta:
        managed = False
        db_table = 'story_character_mask'


class StoryData(models.Model):
    story_group_id = models.IntegerField(primary_key=True)
    story_type = models.IntegerField()
    value = models.IntegerField()
    title = models.TextField()
    thumbnail_id = models.IntegerField()
    disp_order = models.IntegerField()
    start_time = models.TextField()
    end_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'story_data'


class StoryDetail(models.Model):
    story_id = models.IntegerField(primary_key=True)
    story_group_id = models.IntegerField()
    title = models.TextField()
    sub_title = models.TextField()
    visible_type = models.IntegerField()
    story_end = models.IntegerField()
    pre_story_id = models.IntegerField()
    love_level = models.IntegerField()
    requirement_id = models.IntegerField()
    unlock_quest_id = models.IntegerField()
    story_quest_id = models.IntegerField()
    reward_type_1 = models.IntegerField()
    reward_id_1 = models.IntegerField()
    reward_value_1 = models.IntegerField()
    reward_type_2 = models.IntegerField()
    reward_id_2 = models.IntegerField()
    reward_value_2 = models.IntegerField()
    reward_type_3 = models.IntegerField()
    reward_id_3 = models.IntegerField()
    reward_value_3 = models.IntegerField()
    start_time = models.TextField()
    end_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'story_detail'


class StoryQuestData(models.Model):
    story_quest_id = models.IntegerField(primary_key=True)
    story_id = models.IntegerField()
    quest_name = models.TextField()
    limit_time = models.IntegerField()
    background_1 = models.IntegerField()
    wave_group_id_1 = models.IntegerField()
    wave_bgm_sheet_id_1 = models.TextField()
    wave_bgm_que_id_1 = models.TextField()
    background_2 = models.IntegerField()
    wave_group_id_2 = models.IntegerField()
    wave_bgm_sheet_id_2 = models.TextField()
    wave_bgm_que_id_2 = models.TextField()
    background_3 = models.IntegerField()
    wave_group_id_3 = models.IntegerField()
    wave_bgm_sheet_id_3 = models.TextField()
    wave_bgm_que_id_3 = models.TextField()
    guest_unit_1 = models.IntegerField()
    guest_unit_2 = models.IntegerField()
    guest_unit_3 = models.IntegerField()
    guest_unit_4 = models.IntegerField()
    guest_unit_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'story_quest_data'


class Tips(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.IntegerField()
    tips_index = models.IntegerField()
    title = models.TextField()

    class Meta:
        managed = False
        db_table = 'tips'


class TrainingQuestData(models.Model):
    quest_id = models.IntegerField(primary_key=True)
    area_id = models.IntegerField()
    quest_name = models.TextField()
    limit_team_level = models.IntegerField()
    unlock_quest_id_1 = models.IntegerField()
    unlock_quest_id_2 = models.IntegerField()
    stamina = models.IntegerField()
    stamina_start = models.IntegerField()
    team_exp = models.IntegerField()
    unit_exp = models.IntegerField()
    limit_time = models.IntegerField()
    rank_reward_group = models.IntegerField()
    background_1 = models.IntegerField()
    wave_group_id_1 = models.IntegerField()
    wave_bgm_sheet_id_1 = models.TextField()
    wave_bgm_que_id_1 = models.TextField()
    background_2 = models.IntegerField()
    wave_group_id_2 = models.IntegerField()
    wave_bgm_sheet_id_2 = models.TextField()
    wave_bgm_que_id_2 = models.TextField()
    background_3 = models.IntegerField()
    wave_group_id_3 = models.IntegerField()
    wave_bgm_sheet_id_3 = models.TextField()
    wave_bgm_que_id_3 = models.TextField()
    enemy_image_1 = models.IntegerField()
    enemy_image_2 = models.IntegerField()
    enemy_image_3 = models.IntegerField()
    enemy_image_4 = models.IntegerField()
    enemy_image_5 = models.IntegerField()
    reward_image_1 = models.IntegerField()
    reward_image_2 = models.IntegerField()
    reward_image_3 = models.IntegerField()
    reward_image_4 = models.IntegerField()
    reward_image_5 = models.IntegerField()
    training_quest_detail_bg_id = models.IntegerField()
    training_quest_detail_bg_position = models.IntegerField()
    start_time = models.TextField()
    end_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'training_quest_data'


class UnitAttackPattern(models.Model):
    pattern_id = models.IntegerField(primary_key=True)
    unit_id = models.IntegerField()
    loop_start = models.IntegerField()
    loop_end = models.IntegerField()
    atk_pattern_1 = models.IntegerField()
    atk_pattern_2 = models.IntegerField()
    atk_pattern_3 = models.IntegerField()
    atk_pattern_4 = models.IntegerField()
    atk_pattern_5 = models.IntegerField()
    atk_pattern_6 = models.IntegerField()
    atk_pattern_7 = models.IntegerField()
    atk_pattern_8 = models.IntegerField()
    atk_pattern_9 = models.IntegerField()
    atk_pattern_10 = models.IntegerField()
    atk_pattern_11 = models.IntegerField()
    atk_pattern_12 = models.IntegerField()
    atk_pattern_13 = models.IntegerField()
    atk_pattern_14 = models.IntegerField()
    atk_pattern_15 = models.IntegerField()
    atk_pattern_16 = models.IntegerField()
    atk_pattern_17 = models.IntegerField()
    atk_pattern_18 = models.IntegerField()
    atk_pattern_19 = models.IntegerField()
    atk_pattern_20 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'unit_attack_pattern'


class UnitBackground(models.Model):
    unit_id = models.IntegerField(primary_key=True)
    unit_name = models.TextField()
    bg_id = models.IntegerField()
    bg_name = models.TextField()
    position = models.FloatField()
    face_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'unit_background'


class UnitComments(models.Model):
    id = models.IntegerField(primary_key=True)
    unit_id = models.IntegerField()
    use_type = models.IntegerField()
    voice_id = models.IntegerField()
    face_id = models.IntegerField()
    change_time = models.FloatField()
    change_face = models.IntegerField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'unit_comments'


class UnitData(models.Model):
    unit_id = models.IntegerField(primary_key=True)
    unit_name = models.TextField()
    kana = models.TextField()
    prefab_id = models.IntegerField()
    rarity = models.IntegerField()
    motion_type = models.IntegerField()
    se_type = models.IntegerField()
    move_speed = models.IntegerField()
    search_area_width = models.IntegerField()
    atk_type = models.IntegerField()
    normal_atk_cast_time = models.FloatField()
    cutin_1 = models.IntegerField()
    cutin_2 = models.IntegerField()
    guild_id = models.IntegerField()
    exskill_display = models.IntegerField()
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'unit_data'


class UnitEnemyData(models.Model):
    unit_id = models.IntegerField(primary_key=True)
    unit_name = models.TextField()
    prefab_id = models.IntegerField()
    motion_type = models.IntegerField()
    se_type = models.IntegerField()
    move_speed = models.IntegerField()
    search_area_width = models.IntegerField()
    atk_type = models.IntegerField()
    normal_atk_cast_time = models.FloatField()
    cutin = models.IntegerField()
    visual_change_flag = models.IntegerField()
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'unit_enemy_data'


class UnitIntroduction(models.Model):
    id = models.IntegerField(primary_key=True)
    gacha_id = models.IntegerField()
    introduction_number = models.IntegerField()
    start_time = models.TextField()
    end_time = models.TextField()
    maximum_chunk_size_1 = models.IntegerField()
    maximum_chunk_size_loop_1 = models.IntegerField()
    maximum_chunk_size_2 = models.IntegerField()
    maximum_chunk_size_loop_2 = models.IntegerField()
    maximum_chunk_size_3 = models.IntegerField()
    maximum_chunk_size_loop_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'unit_introduction'


class UnitMypagePos(models.Model):
    id = models.IntegerField(primary_key=True)
    pos_x = models.FloatField()
    pos_y = models.FloatField()
    scale = models.FloatField()

    class Meta:
        managed = False
        db_table = 'unit_mypage_pos'


class UnitProfile(models.Model):
    unit_id = models.IntegerField(primary_key=True)
    unit_name = models.TextField()
    age = models.TextField()
    guild = models.TextField()
    race = models.TextField()
    height = models.TextField()
    weight = models.TextField()
    birth_month = models.TextField()
    birth_day = models.TextField()
    blood_type = models.TextField()
    favorite = models.TextField()
    voice = models.TextField()
    voice_id = models.IntegerField()
    catch_copy = models.TextField()
    self_text = models.TextField()
    guild_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'unit_profile'


class UnitPromotion(models.Model):
    unit_id = models.IntegerField(primary_key=True)
    promotion_level = models.IntegerField()
    equip_slot_1 = models.IntegerField()
    equip_slot_2 = models.IntegerField()
    equip_slot_3 = models.IntegerField()
    equip_slot_4 = models.IntegerField()
    equip_slot_5 = models.IntegerField()
    equip_slot_6 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'unit_promotion'
        unique_together = (('unit_id', 'promotion_level'),)


class UnitPromotionStatus(models.Model):
    unit_id = models.IntegerField(primary_key=True)
    promotion_level = models.IntegerField()
    hp = models.FloatField()
    atk = models.FloatField()
    magic_str = models.FloatField()
    def_field = models.FloatField(db_column='def')  # Field renamed because it was a Python reserved word.
    magic_def = models.FloatField()
    physical_critical = models.FloatField()
    magic_critical = models.FloatField()
    wave_hp_recovery = models.FloatField()
    wave_energy_recovery = models.FloatField()
    dodge = models.FloatField()
    physical_penetrate = models.FloatField()
    magic_penetrate = models.FloatField()
    life_steal = models.FloatField()
    hp_recovery_rate = models.FloatField()
    energy_recovery_rate = models.FloatField()
    energy_reduce_rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'unit_promotion_status'
        unique_together = (('unit_id', 'promotion_level'),)


class UnitRarity(models.Model):
    unit_id = models.IntegerField(primary_key=True)
    rarity = models.IntegerField()
    hp = models.FloatField()
    hp_growth = models.FloatField()
    atk = models.FloatField()
    atk_growth = models.FloatField()
    magic_str = models.FloatField()
    magic_str_growth = models.FloatField()
    def_field = models.FloatField(db_column='def')  # Field renamed because it was a Python reserved word.
    def_growth = models.FloatField()
    magic_def = models.FloatField()
    magic_def_growth = models.FloatField()
    physical_critical = models.FloatField()
    physical_critical_growth = models.FloatField()
    magic_critical = models.FloatField()
    magic_critical_growth = models.FloatField()
    wave_hp_recovery = models.FloatField()
    wave_hp_recovery_growth = models.FloatField()
    wave_energy_recovery = models.FloatField()
    wave_energy_recovery_growth = models.FloatField()
    dodge = models.FloatField()
    dodge_growth = models.FloatField()
    physical_penetrate = models.FloatField()
    physical_penetrate_growth = models.FloatField()
    magic_penetrate = models.FloatField()
    magic_penetrate_growth = models.FloatField()
    life_steal = models.FloatField()
    life_steal_growth = models.FloatField()
    hp_recovery_rate = models.FloatField()
    hp_recovery_rate_growth = models.FloatField()
    energy_recovery_rate = models.FloatField()
    energy_recovery_rate_growth = models.FloatField()
    energy_reduce_rate = models.FloatField()
    energy_reduce_rate_growth = models.FloatField()
    unit_material_id = models.IntegerField()
    consume_num = models.IntegerField()
    consume_gold = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'unit_rarity'
        unique_together = (('unit_id', 'rarity'),)


class UnitSkillData(models.Model):
    unit_id = models.IntegerField(primary_key=True)
    union_burst = models.IntegerField()
    main_skill_1 = models.IntegerField()
    main_skill_2 = models.IntegerField()
    main_skill_3 = models.IntegerField()
    main_skill_4 = models.IntegerField()
    main_skill_5 = models.IntegerField()
    main_skill_6 = models.IntegerField()
    main_skill_7 = models.IntegerField()
    main_skill_8 = models.IntegerField()
    main_skill_9 = models.IntegerField()
    main_skill_10 = models.IntegerField()
    ex_skill_1 = models.IntegerField()
    ex_skill_evolution_1 = models.IntegerField()
    ex_skill_2 = models.IntegerField()
    ex_skill_evolution_2 = models.IntegerField()
    ex_skill_3 = models.IntegerField()
    ex_skill_evolution_3 = models.IntegerField()
    ex_skill_4 = models.IntegerField()
    ex_skill_evolution_4 = models.IntegerField()
    ex_skill_5 = models.IntegerField()
    ex_skill_evolution_5 = models.IntegerField()
    sp_skill_1 = models.IntegerField()
    sp_skill_2 = models.IntegerField()
    sp_skill_3 = models.IntegerField()
    sp_skill_4 = models.IntegerField()
    sp_skill_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'unit_skill_data'


class UnitStatusCoefficient(models.Model):
    coefficient_id = models.IntegerField(primary_key=True)
    hp_coefficient = models.FloatField()
    atk_coefficient = models.FloatField()
    magic_str_coefficient = models.FloatField()
    def_coefficient = models.FloatField()
    magic_def_coefficient = models.FloatField()
    physical_critical_coefficient = models.FloatField()
    magic_critical_coefficient = models.FloatField()
    wave_hp_recovery_coefficient = models.FloatField()
    wave_energy_recovery_coefficient = models.FloatField()
    dodge_coefficient = models.FloatField()
    physical_penetrate_coefficient = models.FloatField()
    magic_penetrate_coefficient = models.FloatField()
    life_steal_coefficient = models.FloatField()
    hp_recovery_rate_coefficient = models.FloatField()
    energy_recovery_rate_coefficient = models.FloatField()
    energy_reduce_rate_coefficient = models.FloatField()
    skill_lv_coefficient = models.FloatField()
    exskill_evolution_coefficient = models.IntegerField()
    overall_coefficient = models.FloatField()

    class Meta:
        managed = False
        db_table = 'unit_status_coefficient'


class UnlockSkillData(models.Model):
    promotion_level = models.IntegerField()
    unlock_skill = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'unlock_skill_data'


class UnlockUnitCondition(models.Model):
    unit_id = models.IntegerField(primary_key=True)
    unit_name = models.TextField()
    class_id = models.IntegerField()
    pre_unit_id = models.IntegerField()
    condition_type_1 = models.IntegerField()
    condition_type_detail_1 = models.IntegerField()
    condition_id_1 = models.IntegerField()
    count_1 = models.IntegerField()
    condition_type_2 = models.IntegerField()
    condition_type_detail_2 = models.IntegerField()
    condition_id_2 = models.IntegerField()
    count_2 = models.IntegerField()
    condition_type_3 = models.IntegerField()
    condition_type_detail_3 = models.IntegerField()
    condition_id_3 = models.IntegerField()
    count_3 = models.IntegerField()
    condition_type_4 = models.IntegerField()
    condition_type_detail_4 = models.IntegerField()
    condition_id_4 = models.IntegerField()
    count_4 = models.IntegerField()
    condition_type_5 = models.IntegerField()
    condition_type_detail_5 = models.IntegerField()
    condition_id_5 = models.IntegerField()
    count_5 = models.IntegerField()
    release_effect_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'unlock_unit_condition'


class WaveGroupData(models.Model):
    id = models.IntegerField(primary_key=True)
    wave_group_id = models.IntegerField()
    odds = models.IntegerField()
    enemy_id_1 = models.IntegerField()
    drop_gold_1 = models.IntegerField()
    drop_reward_id_1 = models.IntegerField()
    enemy_id_2 = models.IntegerField()
    drop_gold_2 = models.IntegerField()
    drop_reward_id_2 = models.IntegerField()
    enemy_id_3 = models.IntegerField()
    drop_gold_3 = models.IntegerField()
    drop_reward_id_3 = models.IntegerField()
    enemy_id_4 = models.IntegerField()
    drop_gold_4 = models.IntegerField()
    drop_reward_id_4 = models.IntegerField()
    enemy_id_5 = models.IntegerField()
    drop_gold_5 = models.IntegerField()
    drop_reward_id_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wave_group_data'


class Worldmap(models.Model):
    course_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    map_id = models.IntegerField()
    sheet_id = models.TextField()
    que_id = models.TextField()
    start_area_id = models.IntegerField()
    end_area_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'worldmap'
