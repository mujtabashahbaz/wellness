from rest_framework import serializers
from .models import WellnessLog

class WellnessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WellnessLog
        fields = '__all__'
