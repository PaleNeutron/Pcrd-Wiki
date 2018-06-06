from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Team)
admin.site.register(UnitData)
admin.site.register(SolutionComment)

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ("id" ,"pub_data", "left_team", "right_team", 'up_vote', "down_vote")

    def get_left_team(self, obj):
        return obj.left_team