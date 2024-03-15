from django.views.generic import CreateView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Booking
from .forms import BookingForm

class Bookings(ListView):
    """View all bookings"""

    template_name = "bookings/bookings.html"
    model = Booking
    context_object_name = "bookings"



class AddBooking(LoginRequiredMixin, CreateView):
    """Add booking view"""

    template_name = "bookings/add_booking.html"
    model = Booking
    form_class = BookingForm
    success_url = "/bookings/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddBooking, self).form_valid(form)