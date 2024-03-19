from django.urls import path
from .views import AddSchedule, Schedules, ScheduleDetail, DeleteSchedule, EditSchedule, BookSchedule


urlpatterns = [
    path("add/", AddSchedule.as_view(), name="add_schedule"),
    path("", Schedules.as_view(), name="schedules"),
    path("<slug:pk>/", ScheduleDetail.as_view(), name="schedule_detail"),
    path("delete/<slug:pk>/", DeleteSchedule.as_view(), name="delete_schedule"),
    path("edit/<slug:pk>/", EditSchedule.as_view(), name="edit_schedule"),
    path("book/<slug:pk>/", BookSchedule.as_view(), name="book_schedule"),
]