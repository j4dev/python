from rest_framework import routers
from .api import StudentViewSet
router = routers.DefaultRouter()

router.register('students', StudentViewSet, 'students')

urlpatterns = router.urls