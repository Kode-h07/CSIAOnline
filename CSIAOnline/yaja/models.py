from django.db import models
from django.contrib.auth.models import User


class Monday(models.Model):
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)
    student_id = models.CharField(max_length=10, null=True, blank=True)


class Tuesday(models.Model):
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)
    student_id = models.CharField(max_length=10, null=True, blank=True)


class Wednesday(models.Model):
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)
    student_id = models.CharField(max_length=10, null=True, blank=True)


class Thursday(models.Model):
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)
    student_id = models.CharField(max_length=10, null=True, blank=True)


# Default schedules for users
class DefaultMonday(models.Model):
    student_id = models.CharField(max_length=10, null=True, blank=True)
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)


class DefaultTuesday(models.Model):
    student_id = models.CharField(max_length=10, null=True, blank=True)
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)


class DefaultWednesday(models.Model):
    student_id = models.CharField(max_length=10, null=True, blank=True)
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)


class DefaultThursday(models.Model):
    student_id = models.CharField(max_length=10, null=True, blank=True)
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)
