from django.contrib.sitemaps import Sitemap
from pcrd_unpack.models import UnitProfile, UnitData, EquipmentData, QuestAreaData
from django.urls import reverse
import datetime

class UnitSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1

    def items(self):
        return UnitData.objects.order_by('unit_id').exclude(comment__isnull=True)

    def lastmod(self, obj):
        # todo add data version include date to models
        return datetime.datetime.today()

    def location(self, obj):
        return reverse('pcrd_unpack:unit', kwargs={"unit_id": obj.unit_id})

class EquimpmentSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1

    def items(self):
        return EquipmentData.objects.order_by('equipment_id')

    def lastmod(self, obj):
        # todo add data version include date to models
        return datetime.datetime.today()

    def location(self, obj):
        return reverse('pcrd_unpack:equipment', kwargs={"equipment_id": obj.equipment_id})

class QuestAreaSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1

    def items(self):
        return QuestAreaData.objects.order_by('area_id').filter(area_id__lt=20000)

    def lastmod(self, obj):
        # todo add data version include date to models
        return datetime.datetime.today()

    def location(self, obj):
        return reverse('pcrd_unpack:area_detail', kwargs={"area_id": obj.area_id})