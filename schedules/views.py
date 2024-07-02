from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Schedule
from .forms import ScheduleForm


class Schedules(ListView):
    """View all schedules"""
    template_name = "schedules/schedules.html"
    model = Schedule
    context_object_name = "schedules"

class ScheduleDetail(DetailView):
    """View a single schedule"""
    template_name = "schedules/schedule_detail.html"
    model = Schedule
    context_object_name = "schedule"  

class AddSchedule(LoginRequiredMixin, CreateView):
    """Add schedule view"""
    template_name = "schedules/add_schedule.html"
    model = Schedule
    form_class = ScheduleForm
    success_url = "/schedules/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Schedule added successfully.')
        return super(AddSchedule, self).form_valid(form)

class EditSchedule(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a schedule"""
    template_name = 'schedules/edit_schedule.html'
    model = Schedule
    form_class = ScheduleForm
    success_url = '/schedules/'
    
    def test_func(self):
        messages.success(self.request, 'Schedule modified successfully.')
        return self.request.user == self.get_object().user

class DeleteSchedule(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a schedule"""
    model = Schedule
    success_url = '/schedules/'

    def test_func(self):
        messages.success(self.request, 'Schedule deleted successfully.')
        return self.request.user == self.get_object().user