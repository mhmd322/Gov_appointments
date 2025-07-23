from rest_framework import serializers
from .models import CitizenProfile

class CitizenProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenProfile
        fields = '__all__'
