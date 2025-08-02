# accounts/serializers.py
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import CitizenProfile, UserRole

class APILoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("بيانات الدخول غير صحيحة.")

        try:
            profile = user.citizenprofile
        except CitizenProfile.DoesNotExist:
            raise serializers.ValidationError("لا يوجد ملف شخصي مرتبط بالحساب.")

        refresh = RefreshToken.for_user(user)
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': {
                'username': user.username,
                'email': user.email,
                'role': profile.role,
            }
        }


class APIRegisterSerializer(serializers.ModelSerializer):
    national_id = serializers.CharField(max_length=11)
    phone = serializers.CharField(max_length=14)
    address = serializers.CharField(max_length=255, allow_blank=True)

    class Meta:
        model = User
        fields = ["username", "password", "national_id", "phone", "address"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError({"username": "اسم المستخدم موجود مسبقًا."})
        if CitizenProfile.objects.filter(national_id=data['national_id']).exists():
            raise serializers.ValidationError({"national_id": "الرقم الوطني مستخدم مسبقًا."})
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        CitizenProfile.objects.create(
            user=user,
            role=UserRole.CITIZEN,
            national_id=validated_data['national_id'],
            phone=validated_data['phone'],
            address=validated_data['address'],
        )
        return user
