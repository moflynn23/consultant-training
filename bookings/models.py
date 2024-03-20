from django.db import models

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from schedules.models import Schedule

class Booking(models.Model):
    """
    Model to contain information about a booking.

    :user: Connection to Django's User model.
    :schedule: Connection to Schedule model.
    :creation_date: Date entry was added.

    """
    user = models.ForeignKey(
        User, related_name="bookings", on_delete=models.CASCADE
    )

    schedule = models.ForeignKey(
        Schedule, related_name="schedules", on_delete=models.CASCADE
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
    )
    
    class Meta:
        ordering = ["-creation_date"]

    def __str__(self):
        return str(self.creation_date)