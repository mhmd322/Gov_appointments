# users/serializers.py
from rest_framework import serializers
from users.models import CitizenProfile
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = CitizenProfile
        fields = ['username', 'email', 'national_id', 'phone', 'address', 'role']

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenProfile
        fields = ['phone', 'address']