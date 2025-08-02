# appointments/api_views.py
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.api.permissions import IsCitizen, IsEmployee, IsAdmin
from appointments.models import Appointment
from .serializers import AppointmentSerializer
from django.shortcuts import get_object_or_404

class BookAppointmentView(APIView):
    permission_classes = [IsAuthenticated, IsCitizen]

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyAppointmentsView(APIView):
    permission_classes = [IsAuthenticated, IsCitizen]

    def get(self, request):
        appointments = Appointment.objects.filter(user=request.user).order_by('-date')
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

class EmployeeAppointmentsView(APIView):
    permission_classes = [IsAuthenticated, IsEmployee]

    def get(self, request):
        appointments = Appointment.objects.select_related('user').order_by('-date')
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

class ConfirmAppointmentView(APIView):
    permission_classes = [IsAuthenticated, IsEmployee]

    def post(self, request, appointment_id):
        appointment = get_object_or_404(Appointment, id=appointment_id)
        appointment.confirmed = True
        appointment.save()
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)

class AdminAppointmentsView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        appointments = Appointment.objects.select_related('user').order_by('-date')
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

class EditAppointmentView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def put(self, request, appointment_id):
        appointment = get_object_or_404(Appointment, id=appointment_id)
        serializer = AppointmentSerializer(appointment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
