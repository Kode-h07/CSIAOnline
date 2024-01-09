from django.db import models


# Create your models here.
class Reservation(models.Model):
    timeSlot = models.CharField(max_length=20, unique=True)
    availability = models.BooleanField(default=True)
    id = models.CharField(max_length=10, null=True, blank=True)
