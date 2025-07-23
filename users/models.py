# users/models.py
from django.db import models
from django.contrib.auth.models import User

class UserRole(models.TextChoices):
    CITIZEN = 'citizen', 'مواطن'
    EMPLOYEE = 'employee', 'موظف'
    ADMIN = 'admin', 'مسؤول'

class CitizenProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=UserRole.choices, default=UserRole.CITIZEN)
    national_id = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=14)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"