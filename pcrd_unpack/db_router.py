from django.conf import settings


class DatabaseAppsRouter(object):
    def db_for_read(self, model, **hints):
        app_label = model._meta.app_label
        if app_label in settings.DATABASES_APPS_MAPPING:
            res = settings.DATABASES_APPS_MAPPING[app_label]
            print(res)
            return res
        return None

    def db_for_write(self, model, **hints):
        app_label = model._meta.app_label
        if app_label in settings.DATABASES_APPS_MAPPING:
            return settings.DATABASES_APPS_MAPPING[app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # 获取对应数据库的名字
        db_obj1 = settings.DATABASES_APPS_MAPPING.get(obj1._mata.app_label)
        db_obj2 = settings.DATABASES_APPS_MAPPING.get(obj2._mata.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
        return None

    def db_for_migrate(self, db, app_label, model_name=None, **hints):
        if db in settings.DATABASES_APPS_MAPPING.values():
            return settings.DATABASES_APPS_MAPPING.get(app_label) == db
        elif app_label in settings.DATABASES_APPS_MAPPING:
            return False
        return None