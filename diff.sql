UPDATE event_boss_treasure_content SET odds_1=100, odds_file_2='0', reward_num_2=0, odds_2=0, odds_file_3='0', reward_num_3=0, odds_3=0 WHERE event_boss_treasure_content_id=1000110103;
UPDATE event_boss_treasure_content SET odds_1=100, odds_file_2='0', reward_num_2=0, odds_2=0, odds_file_3='0', reward_num_3=0, odds_3=0 WHERE event_boss_treasure_content_id=1000210103;
UPDATE event_boss_treasure_content SET odds_1=100, odds_file_2='0', reward_num_2=0, odds_2=0, odds_file_3='0', reward_num_3=0, odds_3=0 WHERE event_boss_treasure_content_id=1000310103;
DELETE FROM event_gacha_data WHERE gacha_id=10003;
INSERT INTO event_gacha_data(gacha_id,event_id,gacha_name,item_type,item_id,cost,repeat_step) VALUES(19003,10003,'ヴァンパイアハンターwithイリヤ討伐証交換',2,60022,1,5);
