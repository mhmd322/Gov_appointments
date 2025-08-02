from rest_framework.permissions import BasePermission
from users.models import UserRole

class IsCitizen(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'citizenprofile', None) and request.user.citizenprofile.role == UserRole.CITIZEN

class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'citizenprofile', None) and request.user.citizenprofile.role == UserRole.EMPLOYEE

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'citizenprofile', None) and request.user.citizenprofile.role == UserRole.ADMIN

