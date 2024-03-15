from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """Form to create a booking"""

    class Meta:
        model = Booking
        fields = [
            "title",
            "date_from",
            "date_until"
        ]

        labels = {
            "title": "Booking Title",
            "date_from": "From",
            "date_until": "Until",
        }