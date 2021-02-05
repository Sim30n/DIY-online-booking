from django.contrib import admin
from .models import Service, Reservation, Freetime

# Register your models here.
admin.site.register(Service)
admin.site.register(Reservation)
admin.site.register(Freetime)
