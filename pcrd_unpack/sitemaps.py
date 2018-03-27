from django.contrib.sitemaps import Sitemap
from pcrd_unpack.models import UnitProfile, UnitData, EquipmentData
from django.urls import reverse
import datetime

class UnitSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1

    def items(self):
        return UnitData.objects.exclude(comment__isnull=True)

    def lastmod(self, obj):
        # todo add data version include date to models
        return datetime.datetime.today()

    def location(self, obj):
        return reverse('pcrd_unpack:unit', kwargs={"unit_id": obj.unit_id})

class EquimpmentSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1

    def items(self):
        return EquipmentData.objects.all()

    def lastmod(self, obj):
        # todo add data version include date to models
        return datetime.datetime.today()

    def location(self, obj):
        return reverse('pcrd_unpack:equipment', kwargs={"equipment_id": obj.equipment_id})