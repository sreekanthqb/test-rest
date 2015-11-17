from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % (self.name)


class Branch(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return "%s" % (self.name)


class College(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True, blank=True)
    courses = models.ManyToManyField(Course, blank=True)

    def __unicode__(self):
        return "%s" % (self.name)


class CollegeCourse(models.Model):
    college = models.ForeignKey(College)
    course = models.ForeignKey(Course)
    branch = models.ForeignKey(Branch)
    year = models.IntegerField()

    def __unicode__(self):
        return "%s - %s - %s - %d" % (self.name, self.course, self.branch, self.year)
