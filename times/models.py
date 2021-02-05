from django.db import models
import datetime

class Freetime(models.Model):
    operator = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

# Create your models here.
class Service(models.Model):
    service_type = models.CharField(max_length=200)
    duration = models.IntegerField()
    description = models.TextField()
    break_time = models.IntegerField()

    def get_extended_duration(self):
        return self.duration + self.break_time


class Reservation(models.Model):
    operator = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    service = models.ForeignKey('times.Service',
                                related_name="services",
                                on_delete=models.CASCADE)
    reserved_date = models.DateTimeField()
    description = models.TextField()
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_tel = models.CharField(max_length=200)

    def get_end_time(self):
        return self.reserved_date + datetime.timedelta(minutes=self.service.get_extended_duration())
