from django.views.generic import CreateView, ListView, TemplateView

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Booking
from schedules.models import Schedule

from django.db import models
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Booking
from .forms import BookingForm


class Bookings(ListView):
    model = Booking
    template_name = "bookings/bookings.html"
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.select_related('schedule').all()

# views.py in your app (e.g., bookings/views.py)

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from schedules.models import Schedule
from .models import Booking
from django.contrib import messages

@login_required
@require_POST
def create_booking(request, schedule_id):
    user = request.user
    schedule = get_object_or_404(Schedule, id=schedule_id)
    Booking.objects.create(user=user, schedule=schedule)
    messages.success(request, 'Booked successfully.')
    return HttpResponseRedirect(reverse('schedule_detail', args=[schedule_id]))  # Redirect to schedule detail or booking success page

