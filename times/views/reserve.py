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
        initial["description"] = "MORO MORO"
        return initial


class ThankYouView(TemplateView):

    template_name = "times/thankyou.html"
