from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActiveUserViewSet, active_users_view

router = DefaultRouter()
router.register(r'active-users', ActiveUserViewSet, basename="active-users")

active_user_view_path =  path('active-users-charts/', active_users_view, name='active_users_charts'),
urlpatterns = router.urls 

urlpatterns += active_user_view_path

