from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=100)


class College(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True, blank=True)
    courses = models.ManyToManyField(Course, blank=True)
