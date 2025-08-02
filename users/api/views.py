# users/api_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from accounts.api.permissions import IsCitizen, IsEmployee
from users.api.serializers import UserProfileSerializer, UpdateProfileSerializer

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = getattr(request.user, 'citizenprofile', None)
        if profile:
            serializer = UserProfileSerializer(profile)
            return Response(serializer.data)
        return Response({'error': 'لا يوجد ملف شخصي'}, status=404)

class UpdateUserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        profile = getattr(request.user, 'citizenprofile', None)
        if profile:
            serializer = UpdateProfileSerializer(profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'detail': 'تم تحديث الملف الشخصي بنجاح'})
            return Response(serializer.errors, status=400)
        return Response({'error': 'لا يوجد ملف شخصي'}, status=404)
