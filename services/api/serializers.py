# services/serializers.py
from rest_framework import serializers
from services.models import Service, Request

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'requires_documents']

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'service', 'full_name', 'national_id', 'submitted_at', 'status']
        read_only_fields = ['id', 'submitted_at', 'status']
