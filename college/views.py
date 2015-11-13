from rest_framework import viewsets
from college.serializers import CollegeSerializer
from college.models import College


class CollegeViewSet(viewsets.ModelViewSet):
    serializer_class = CollegeSerializer
    queryset = College.objects.all()
