from rest_framework import serializers
from .models import ActiveUser

class ActiveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveUser
        fields = "__all__"
