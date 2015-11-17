from rest_framework import serializers
from college.models import College, Course


class CollegeSerializer(serializers.ModelSerializer):

    class Meta:
        model = College
        exclude = []


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ["id", "name", "test_status"]
