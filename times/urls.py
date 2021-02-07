from django.urls import path
from . import views

#app_name = "website"

urlpatterns = [
    path("timetable/<str:week>", views.TimeTableView.as_view(), name='timetable'),
    path("reserve/<str:week>/<str:time>", views.ReserveView.as_view(success_url="/thankyou"), name='reservation'),
    path("thankyou/", views.ThankYouView.as_view(), name="thankyou")
]
