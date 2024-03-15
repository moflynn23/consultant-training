from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "date_from",
        "date_until",
        "creation_date",
        "time_period",
        "time_unit",
    )
    list_filter = ("date_from",)