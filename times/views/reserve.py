from django.shortcuts import render, redirect
from times.models import Freetime, Service, Reservation
from times.forms import ReserveForm
from django.views.generic import (CreateView, TemplateView)
import datetime
from pytz import timezone
# Create your views here.

class ReserveView(CreateView):
    form_class = ReserveForm
    model = Reservation

    def get_initial(self):
        initial = super(ReserveView, self).get_initial()
        initial = initial.copy()
        print(self.kwargs)
        res_time = self.kwargs["res_time"].split()
        print(res_time[0])
        res_date = self.kwargs["res_date"]
        res_datetime = datetime.datetime.strptime("{} {}".format(res_time[0], res_date), "%H:%M %d.%m.%y")
        initial["reserved_date"] = res_datetime
        return initial


class ThankYouView(TemplateView):

    template_name = "times/thankyou.html"

class ServiceChoiceView(TemplateView):
    template_name = "times/service_choice.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context
