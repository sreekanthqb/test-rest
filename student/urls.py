from django.conf.urls import url, include
from rest_framework import routers
from student.views import StudentViewSet

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'students', StudentViewSet,)


urlpatterns = [
    url(r'^api/', include(router.urls)),
]
