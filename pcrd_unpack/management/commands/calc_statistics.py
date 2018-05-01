import os
import itertools
import logging
import dukpy
from django.core.management.base import BaseCommand, CommandError
from django.contrib.staticfiles import finders

from pcrd_unpack.models import QuestRewardDataCustom, QuestData, WaveGroupData, EnemyRewardData, EquipmentData, \
    ItemData, HatsuneQuest, HatsuneQuestRewardDataCustom, UnitData, UnitSummary
from django.db import transaction
from pcrd_unpack.views import UnitJsonView, UnitDetailView, UnitListView

logger = logging.getLogger("main")


class Command(BaseCommand):
    help = 'calculate all statistics'

    def handle(self, *args, **options):
        self.calc()
        self.calcUnit()

    @transaction.atomic
    def calcUnit(self):
        UnitSummary.objects.all().delete()
        max_level = UnitSummary.max_level()
        max_rank = UnitSummary.max_rank()
        max_rarity = UnitSummary.max_rarity()

        js_path = finders.find("pcrd_unpack/scripts/elements/UnitDataModel.js")
        with open(js_path) as f:
            es6js = f.read()
        es5js = dukpy.babel_compile(es6js)["code"]
        jsi = dukpy.JSInterpreter()

        for u in UnitListView().get_queryset():
            unit_id = u.unit_id
            data = UnitJsonView().get_unit_data(unit_id=unit_id)
            context_data = UnitDetailView().get_context_data(unit_id=unit_id)

            # new an instant once of one calc, due to the dukpy bug
            r = jsi.evaljs([es5js,
                            "var udm = new UnitDataModel()",
                            "udm.unit_parameter = dukpy['value']",
                            "udm.result_ids = dukpy['data_tags']",
                            "udm.calc(dukpy['max_level'],dukpy['max_rank'],dukpy['max_rarity'])",
                            "udm;"], max_level=max_level, max_rank=max_rank, max_rarity=max_rarity,
                           value=data, data_tags=context_data["data_tags"])
            us = UnitSummary(unit_id=unit_id)
            for p in context_data["data_tags"]:
                setattr(us, p, r[p])
            us.save()

    @transaction.atomic
    def calc(self):
        # todo VERY!!!!!! slow, need research
        QuestRewardDataCustom = globals()["QuestRewardDataCustom"]
        QuestData = globals()["QuestData"]

        q_list = []
        QuestRewardDataCustom.objects.all().delete()
        for qd in QuestData.objects.all():
            print("****quest {}****".format(qd.quest_id))
            wg1 = qd.wave_group_id_1
            wg2 = qd.wave_group_id_2
            wg3 = qd.wave_group_id_3
            wgd_all = WaveGroupData.objects.filter(wave_group_id__in=[wg1, wg2, wg3]).all()
            dr_ids = [(i.drop_reward_id_1, i.drop_reward_id_2, i.drop_reward_id_3,
                       i.drop_reward_id_4, i.drop_reward_id_5)
                      for i in wgd_all]
            dr_ids = itertools.chain.from_iterable(dr_ids)
            dr_ids = [i for i in dr_ids if i != 0]
            for dr_id in dr_ids:
                er = EnemyRewardData.objects.get(drop_reward_id=dr_id)
                for i in range(1, 6):
                    r_id = getattr(er, "reward_id_{}".format(i))
                    r_rate = getattr(er, "odds_{}".format(i))
                    if r_id > 100000:
                        q = QuestRewardDataCustom(quest=qd, equipment=EquipmentData.objects.get(equipment_id=r_id),
                                                  rate=r_rate)
                    elif r_id > 0:
                        q = QuestRewardDataCustom(quest=qd, item=ItemData.objects.get(item_id=r_id),
                                                  rate=r_rate)
                    else:
                        continue
                    print("reward: {}, rate: {}".format(r_id, r_rate))
                    q_list.append(q)

        QuestRewardDataCustom.objects.bulk_create(q_list)

    @transaction.atomic
    def calc_hatsune(self):
        pass
