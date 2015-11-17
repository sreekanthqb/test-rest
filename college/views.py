from rest_framework import viewsets
from rest_framework.response import Response

from college.serializers import CollegeSerializer, CourseSerializer
from college.models import College, Course


class CollegeViewSet(viewsets.ModelViewSet):
    serializer_class = CollegeSerializer
    queryset = College.objects.all()


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            for course in page:
                course.test_status = True
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        self.check_object_permissions(self.request, self.kwargs['pk'])
        course = self.get_queryset().get(id=self.kwargs['pk'])
        course.test_status = True
        serializer = self.get_serializer(course)
        return Response(serializer.data)
