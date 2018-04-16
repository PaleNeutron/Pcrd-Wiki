import os
import argparse
import sqlite3
import logging
from django.core.management.base import BaseCommand, CommandError
from pcrd_unpack.models import QuestRewardDataCustom, QuestData, WaveGroupData, EnemyRewardData, EquipmentData, \
    ItemData, HatsuneQuest, HatsuneQuestRewardDataCustom
from django.db import transaction


logger = logging.getLogger("django")
logger.setLevel(logging.DEBUG)


def sqlite_db(path):
    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError('%s is not a file' % path)

    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    # test if this is really sqlite file
    cur = conn.cursor()
    cur.execute('SELECT 1 from sqlite_master where type = "table"')
    try:
        data = cur.fetchone()
    except sqlite3.DatabaseError:
        msg = '%s can\'t be read as SQLite DB' % path
        raise argparse.ArgumentTypeError(msg)

    return conn


# parser = argparse.ArgumentParser(description='Merge data from src to dest db')
# parser.add_argument('src_db', type=sqlite_db,
#                     help='Source DB file path')
# parser.add_argument('dst_db', type=sqlite_db,
#                     help='Destination DB file path')
#
# args = parser.parse_args()
def update_db(src_path, dst_path):
    src_db = sqlite_db(src_path)
    dst_db = sqlite_db(dst_path)
    src_cur = src_db.cursor()
    dst_cur = dst_db.cursor()

    src_cur.execute('SELECT * from sqlite_master')
    src_master = src_cur.fetchall()

    src_tables = filter(lambda r: r['type'] == 'table' and not r['name'].startswith("sqlite"), src_master)
    src_indices = filter(lambda r: r['type'] == 'index' and r['sql'] is not None, src_master)

    # logger.info('Found tables: %d', len(src_tables))
    for table in src_tables:
        logger.info('Processing table: %s', table['name'])

        logger.info('Delete old table in destination db, if exists')
        dst_cur.execute("DROP TABLE IF EXISTS " + table['name'])

        logger.info('Creating table structure')
        logger.debug('SQL: %s', table['sql'])
        dst_cur.execute(table['sql'])

        logger.info('Moving data')
        src_cur.execute('SELECT COUNT(1) AS cnt FROM %s' % table['name'])
        total_rows = src_cur.fetchone()['cnt']
        logger.debug('Rows: %d', total_rows)

        src_cur.execute('SELECT * FROM %s' % table['name'])
        item = 0
        for row in src_cur:
            item += 1
            if item % 50000 == 0:
                logger.debug('Processing %d / %d', item, total_rows)
                dst_db.commit()

            cols = row.keys()
            query = 'INSERT INTO %(tbl)s (%(cols)s) VALUES (%(phold)s)' % {
                'tbl': table['name'],
                'cols': ','.join(cols),
                'phold': ','.join(('?',) * len(cols))
            }
            dst_cur.execute(query, [row[col] for col in cols])

        dst_db.commit()

        logger.info('Creating table indices')
        table_idx = filter(lambda r: r['tbl_name'] == table['name'], src_indices)
        # logger.info('Found indices: %d', len(list(table_idx)))
        for idx in table_idx:
            logger.debug('SQL: %s', idx['sql'])
            dst_cur.execute(idx['sql'])

        logger.info('Finished with %s', table['name'])

    src_db.close()
    dst_db.close()

class Command(BaseCommand):
    help = 'update database from source master.mdb'

    def handle(self, *args, **options):
        update_db("../jp.co.cygames.princessconnectredive/files/manifest/7d2bdcfa272ce3dadad2c2094b496a0ab1176aeb" , 'pcrd_db/pcrdwiki.db')

