from django.urls import path
from .views import AddBooking, Bookings


urlpatterns = [
    path("", AddBooking.as_view(), name="add_booking"),
    path("bookings/", Bookings.as_view(), name="bookings"),
]