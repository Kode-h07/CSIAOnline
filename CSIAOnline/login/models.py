from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30,default=True)