from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20, unique=True)
    last_name = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=20,default=True)
    color = models.CharField(max_length=10, null=True, blank=True)