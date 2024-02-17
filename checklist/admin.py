from django.contrib import admin

from checklist.models import (
    ChecklistItem,
    DailyActivityChecklist,
    DefaultChecklistItem,
    QuranChecklist,
    SalahChecklist,
)


@admin.register(QuranChecklist)
class QuranChecklistAdmin(admin.ModelAdmin):
    pass


@admin.register(SalahChecklist)
class SalahChecklistAdmin(admin.ModelAdmin):
    pass


@admin.register(DailyActivityChecklist)
class DailyActivityChecklistAdmin(admin.ModelAdmin):
    pass


@admin.register(DefaultChecklistItem)
class DefaultChecklistItemAdmin(admin.ModelAdmin):
    pass


@admin.register(ChecklistItem)
class ChecklistItemAdmin(admin.ModelAdmin):
    pass
