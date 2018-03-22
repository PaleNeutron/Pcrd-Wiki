import os
import itertools
import logging
from django.core.management.base import BaseCommand, CommandError
from pcrd_unpack.models import QuestRewardDataCustom, QuestData, WaveGroupData, EnemyRewardData, EquipmentData,   \
    ItemData
from django.db import transaction


logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'calculate all statistics'

    def handle(self, *args, **options):
        self.calc()

    @transaction.atomic
    def calc(self):
        # todo VERY!!!!!! slow, need research
        QuestRewardDataCustom.objects.all().delete()
        q_list = []
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



