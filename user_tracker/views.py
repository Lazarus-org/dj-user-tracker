from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAdminUser
from django.utils.timezone import now
from django.shortcuts import render

from datetime import timedelta
from .models import ActiveUser
from .serializers import ActiveUserSerializer

class ActiveUserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ActiveUserSerializer
    # permission_classes = [IsAdminUser]  # Only admins can access

    def get_queryset(self):
        threshold = now() - timedelta(minutes=10)  # Consider users active within the last 10 minutes
        return ActiveUser.objects.filter(last_activity__gte=threshold)



def active_users_view(request):
    threshold = now() - timedelta(minutes=10)
    active_users = ActiveUser.objects.select_related("user").filter(last_activity__gte=threshold).order_by('-last_activity')
    context = {
        'active_users': active_users
    }
    return render(request, 'active_users.html', context)