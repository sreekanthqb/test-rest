from django.contrib import admin
from college.models import College, Course, Branch, CollegeCourse

admin.site.register(College)
admin.site.register(Course)
admin.site.register(Branch)
admin.site.register(CollegeCourse)
