from django.contrib import admin
from .models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "date_from",
        "date_until",
        "details",
        "location",
        "creation_date",
    )
    list_filter = ("location",)