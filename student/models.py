from django.db import models
from django.contrib.auth.models import User
from college.models import College


class Student(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True, blank=True)


class StudentCollegeMap(models.Model):
    student = models.ForeignKey(Student)
    college = models.ForeignKey(College)
    year = models.CharField(max_length=10, null=True, blank=True)
