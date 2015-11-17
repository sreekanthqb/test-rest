import logging
from rest_framework import viewsets
from student.serializers import StudentSerializer
from student.models import Student

logger = logging.getLogger(__name__)


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def get_queryset(self):
        logger.error('Something went wrong!')
        return self.queryset
