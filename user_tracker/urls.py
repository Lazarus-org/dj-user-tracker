from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActiveUserViewSet

router = DefaultRouter()
router.register(r'active-users', ActiveUserViewSet, basename="active-users")

urlpatterns = router.urls
