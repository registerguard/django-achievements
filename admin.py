from django.contrib import admin
from achievements.models import Achievement, Town

class TownAdmin(admin.ModelAdmin):
    pass

admin.site.register(Town, TownAdmin)

class AchievementAdmin(admin.ModelAdmin):
    list_display = ('first_name_middle', 'last_name', 'date', 'short_description',)
    list_display_links = ('first_name_middle', 'last_name',)
    list_editable = ('short_description',)

admin.site.register(Achievement, AchievementAdmin)
