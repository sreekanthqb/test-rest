from django.db import models
from django.contrib.auth.models import User
from college.models import College, CollegeCourse


class Student(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return "%s" % (self.user.get_full_name())


class StudentCollegeMap(models.Model):
    student = models.ForeignKey(Student)
    college = models.ForeignKey(College)
    course = models.ForeignKey(CollegeCourse)

    def __unicode__(self):
        return "%s - %s" % (self.student, self.college)
