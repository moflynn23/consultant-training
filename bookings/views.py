from django.views.generic import CreateView, ListView

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Booking


class Bookings(ListView):
    """View all bookings"""

    template_name = "bookings/bookings.html"
    model = Booking
    context_object_name = "bookings"