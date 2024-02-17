from django.contrib import admin

from org.models import LocationOffset


@admin.register(LocationOffset)
class LocationOffsetAdmin(admin.ModelAdmin):
    pass
