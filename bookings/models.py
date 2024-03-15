from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    """
    Model to contain information about a booking.

    :user (optional): Connection to Django's User model.
    :title (optional): Title of the booking.
    :date_from (optional): From when the booking is active.
    :date_until (optional): Until when the booking is active.
    :time_period (optional): How long the period from date_from will be.
      e.g.: 10 (days).
    :time_unit (optional): What unit of time the period is of. e.g. nights or
      days.
    :creation_date: Date of the booking.
    :booking_status: Current status of the booking.

    """
    user = models.ForeignKey(
        User, related_name="bookings", on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=300, 
        null=False, blank=False
    )

    date_from = models.DateTimeField(
        blank=True, null=True,
    )

    date_until = models.DateTimeField(
        blank=True, null=True,
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
    )
    time_period = models.PositiveIntegerField(
        blank=True, null=True,
    )

    time_unit = models.CharField(
        default=getattr(settings, 'BOOKING_TIME_INTERVAL', ''),
        max_length=64,
        blank=True,
    )

    class Meta:
        ordering = ["-creation_date"]

    def __str__(self):
        return str(self.title)