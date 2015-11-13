from django.conf.urls import url, include
from rest_framework import routers
from college.views import CollegeViewSet

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'colleges', CollegeViewSet,)


urlpatterns = [
    url(r'^api/', include(router.urls)),
]
