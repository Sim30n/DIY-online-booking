from django.urls import path
from . import views

#app_name = "website"

urlpatterns = [
    path("timetable/<str:week>/<int:duration>", views.TimeTableView.as_view(), name='timetable'),
    path("reserve/<str:res_time>/<str:res_date>", views.ReserveView.as_view(success_url="/thankyou"), name='reservation'),
    path("thankyou/", views.ThankYouView.as_view(), name="thankyou"),
    path("servicechoice/", views.ServiceChoiceView.as_view(), name="servicechoice")
]
