# forms.py in your app (e.g., bookings/forms.py)

from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'schedule']
