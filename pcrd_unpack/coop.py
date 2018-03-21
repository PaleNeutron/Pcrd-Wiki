import sqlite3
import os
from PcrdWiki.settings import BASE_DIR



#
#
# items = [i for i in c.execute('SELECT repeat_reward_image_3 FROM cooperation_quest_data')]
# for i in items:
#     print i

def get_drop_string():
    c = sqlite3.connect(os.path.join(BASE_DIR, "pcrd_db", '7d2bdcfa272ce3dadad2c2094b496a0ab1176aeb'))

    def query_group(id):
        t = (id,)
        row = [i for i in c.execute(
            'SELECT drop_reward_id_1,drop_reward_id_2,drop_reward_id_3,drop_reward_id_4,drop_reward_id_5 FROM wave_group_data WHERE wave_group_id=?',
            t)][0]
        return row

    def query_equip(id):
        t = (id,)
        row = [i for i in c.execute('SELECT * FROM equipment_data WHERE equipment_id=?', t)][0]
        return row[0], row[1], row[2]

    def query_item(id):
        t = (id,)
        row = [i for i in c.execute('SELECT * FROM item_data WHERE item_id=?', t)][0]
        return row[1], row[2]

    def query_reward(id):
        t = (id,)
        row = [i for i in
               c.execute('SELECT reward_id_1,reward_id_2,reward_id_3 FROM quest_reward_data WHERE reward_group_id=?',
                         t)][0]
        return row

    def query_enemy_reward(id):
        t = (id,)
        row = [i for i in
               c.execute(
                   'SELECT reward_id_1,reward_id_2,reward_id_3,reward_id_4,reward_id_5,odds_1,odds_2,odds_3,odds_4,odds_5 FROM enemy_reward_data WHERE drop_reward_id=?',
                   t)][0]
        return row

    items = [i for i in c.execute('SELECT quest_name,wave_group_id_1,wave_group_id_2,wave_group_id_3 FROM quest_data')]
    quest_list = []
    for i in items:
        quest = []
        # print()
        # print("=======",i[0],"=========")
        quest.append(i[0])
        # print("[collapse]")
        for j in range(1, 4):

            reward = [a for a in query_group(i[j]) if a != 0]
            #print(reward)
            for k in reward:
                #print(k)
                ene_rew = query_enemy_reward(k)
                #print(ene_rew)
                for l in range(5):
                    if (ene_rew[l]!=0):
                        try:
                            # print("ITEM: %s" % query_equip(ene_rew[l])[0])
                            # print("DROP RATE:", ene_rew[l+5])
                            quest.append(query_equip(ene_rew[l])[0])

                        except Exception:
                            pass



            # print(query_reward(k))
        # print("[/collapse]")
        quest_list.append(quest)
    return quest_list
