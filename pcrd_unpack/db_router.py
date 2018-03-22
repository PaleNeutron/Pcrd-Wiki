

class DatabaseCustomRouter(object):
    pass
    ## Django doesn’t currently provide any support for foreign key or many-to-many relationships spanning multiple databases
    ## Remove this Router

    # def __init__(self):
    #     self.db_name = 'pcrd_custom_db'
    #     self.app_label = 'pcrd_unpack'
    #     self._custom_models = ["QuestRewardDataCustom"]
    #     self.custom_models = [self.app_label + "." + i for i in self._custom_models]
    #
    # def in_this_db(self, model):
    #     return model._meta.label in self.custom_models
    #
    # def db_for_read(self, model, **hints):
    #     """
    #     Attempts to read pcrd_unpack models go to pcrd_db.
    #     """
    #
    #     if self.in_this_db(model) and model._meta.app_label == self.app_label:
    #         return self.db_name
    #     return None
    #
    # def db_for_write(self, model, **hints):
    #     """
    #     Attempts to write pcrd_unpack models go to pcrd_db.
    #     """
    #     if self.in_this_db(model) and model._meta.app_label == self.app_label:
    #         return self.db_name
    #     return None
    #
    # def allow_relation(self, obj1, obj2, **hints):
    #     """
    #     Allow relations if a model in the pcrd_unpack app is involved.
    #     """
    #
    #     if obj1._meta.app_label == self.app_label or \
    #             obj2._meta.app_label == self.app_label:
    #         return True
    #     return None
    #
    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #     """
    #     Make sure the pcrd_unpack app only appears in the 'pcrd_db'
    #     database.
    #     """
    #     if 'model' in hints:
    #         if self.in_this_db(hints['model']) and app_label == self.app_label:
    #             return db == self.db_name
    #     return None


class DatabaseUnpackedRouter(object):
    db_name = 'pcrd_db'
    app_label = 'pcrd_unpack'
    def db_for_read(self, model, **hints):
        """
        Attempts to read pcrd_unpack models go to pcrd_db.
        """
        if model._meta.app_label == self.app_label:
            return self.db_name
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write pcrd_unpack models go to pcrd_db.
        """
        if model._meta.app_label == self.app_label:
            return self.db_name
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the pcrd_unpack app is involved.
        """
        if obj1._meta.app_label == self.app_label or \
                obj2._meta.app_label == self.app_label:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the pcrd_unpack app only appears in the 'pcrd_db'
        database.
        """
        if app_label == self.app_label:
            return db == self.db_name
        return None


class DefaultRouter(object):
    db_name = 'default'
    def db_for_read(self, model, **hints):
        """
        Attempts to read pcrd_unpack models go to pcrd_db.
        """

        return self.db_name


    def db_for_write(self, model, **hints):
        """
        Attempts to write pcrd_unpack models go to pcrd_db.
        """

        return self.db_name


    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the pcrd_unpack app is involved.
        """

        if obj1._state.db == obj2._state.db:
            return True
        return False


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the pcrd_unpack app only appears in the 'pcrd_db'
        database.
        """
        return db == self.db_name