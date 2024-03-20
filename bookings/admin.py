from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "schedule",
        "creation_date",
    )
    list_filter = ("creation_date",)