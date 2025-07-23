# users/admin.py
from django.contrib import admin
from .models import CitizenProfile

@admin.register(CitizenProfile)
class CitizenProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'national_id', 'phone']
    list_filter = ['role']
    search_fields = ['user__username', 'national_id']
