from django.apps import AppConfig
# import sqlite3
# from io import StringIO
# from django.conf import settings
# from django.db import connections

class PcrdUnpackConfig(AppConfig):
    name = 'pcrd_unpack'
    # def ready(self):
    #     self.init_sqlite_db()
    #
    #
    # def init_sqlite_db(self):
    #     # Read database to tempfile
    #     con = sqlite3.connect(settings.DATABASES["pcrd_db_indisk"]["NAME"])
    #     tempfile = StringIO()
    #     for line in con.iterdump():
    #         tempfile.write('%s\n' % line)
    #     con.close()
    #     tempfile.seek(0)
    #
    #     # Create a database in memory and import from tempfile
    #     self.sqlite = sqlite3.connect(":memory:")
    #     self.sqlite.cursor().executescript(tempfile.read())
    #     self.sqlite.commit()
    #     self.sqlite.row_factory = sqlite3.Row