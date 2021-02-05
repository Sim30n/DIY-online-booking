from django.urls import path
from . import views

#app_name = "website"

urlpatterns = [
    path("timetable/<str:week>", views.TimeTableView.as_view(), name='timetable'),
]
