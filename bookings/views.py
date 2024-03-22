from django.views.generic import CreateView, ListView, TemplateView

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Booking
from schedules.models import Schedule

from django.db import models


class Bookings(ListView):
    model = Booking
    template_name = "bookings/bookings.html"
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.select_related('schedule').all()