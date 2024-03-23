from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

LOCATIONS = (
    ("cork", "Cork"),
    ("dublin", "Dublin"),
    ("kerry", "Kerry"),
)

class Schedule(models.Model):
    """
    Model to contain information about a schedule.

    :user: Connection to Django's User model.
    :title: Title of the schedule.
    :date_from: For when the schedule is active from.
    :date_until: For when the schedule is active until.
    :details (optional): Details of the schedule.
    :location: Location of the schedule.
    :creation_date: Date entry was added.

    """
    user = models.ForeignKey(
        User, related_name="schedules", on_delete=models.CASCADE
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

    details = models.CharField(
        max_length=500, 
        null=False, blank=False
    )

    location = models.CharField(
        max_length=50, choices=LOCATIONS, default="cork"
    )

    creation_date = models.DateTimeField(
        auto_now_add=True,
    )
    
    class Meta:
        ordering = ["creation_date"]

    def __str__(self):
        return str(self.title)