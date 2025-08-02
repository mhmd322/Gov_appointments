# appointments/serializers.py
from rest_framework import serializers
from appointments.models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'user', 'date', 'time', 'reason', 'confirmed']
        read_only_fields = ['id', 'user', 'confirmed']