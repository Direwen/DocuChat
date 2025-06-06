from rest_framework import routers
from .views import DocumentViewSet

router = routers.DefaultRouter()
router.register('', DocumentViewSet)

urlpatterns = router.urls
