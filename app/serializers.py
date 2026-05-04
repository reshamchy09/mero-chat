from rest_framework import serializers
from .models import AppUpdate

class AppUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUpdate
        fields = '__all__'