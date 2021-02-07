from django import forms
from times.models import Service, Freetime, Reservation

class ReserveForm(forms.ModelForm):

    class Meta():
        model = Reservation
        fields = '__all__'
