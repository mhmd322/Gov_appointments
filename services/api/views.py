# services/api_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from accounts.api.permissions import IsCitizen, IsEmployee
from services.models import Service, Request
from .serializers import ServiceSerializer, RequestSerializer

class ServiceListView(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

class SubmitRequestView(APIView):
    permission_classes = [IsAuthenticated, IsCitizen]

    def post(self, request):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyRequestsView(APIView):
    permission_classes = [IsAuthenticated, IsCitizen]

    def get(self, request):
        requests = Request.objects.filter(user=request.user).order_by('-submitted_at')
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)

class EmployeeRequestListView(APIView):
    permission_classes = [IsAuthenticated, IsEmployee]

    def get(self, request):
        requests = Request.objects.select_related('user', 'service').order_by('-submitted_at')
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)

class UpdateRequestStatusView(APIView):
    permission_classes = [IsAuthenticated, IsEmployee]

    def post(self, request, request_id):
        req = get_object_or_404(Request, id=request_id)
        new_status = request.data.get('status')
        valid_statuses = dict(Request._meta.get_field('status').choices).keys()
        if new_status in valid_statuses:
            req.status = new_status
            req.save()
            serializer = RequestSerializer(req)
            return Response(serializer.data)
        return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)
