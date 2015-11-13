from rest_framework import viewsets
from student.serializers import StudentSerializer
from student.models import Student


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
