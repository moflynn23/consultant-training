from django import forms
from .models import Schedule


class ScheduleForm(forms.ModelForm):
    """Form to create a schedule"""

    class Meta:
        model = Schedule
        fields = [
            "title",
            "date_from",
            "date_until",
            "details",
            "location",
        ]

        labels = {
            "title": "Schedule Title",
            "date_from": "From",
            "date_until": "Until",
            "details": "Details",
            "location": "Location",
        }