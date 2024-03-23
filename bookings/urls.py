from django.urls import path
from .views import Bookings, create_booking


urlpatterns = [
    path("", Bookings.as_view(), name="bookings"),
    path('<int:schedule_id>/book/', create_booking, name='create_booking'),
]