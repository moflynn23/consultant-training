from django import forms
from .models import Schedule

from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput


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

        widgets = {
            'date_from': DateTimePickerInput(attrs={'class': 'datepicker', 'id': 'date_from'}),
            'date_until': DateTimePickerInput(attrs={'class': 'datepicker', 'id': 'date_until'}),
        }

        labels = {
            "title": "Schedule Title",
            "date_from": "From",
            "date_until": "Until",
            "details": "Details",
            "location": "Location",
        }