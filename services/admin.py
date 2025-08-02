from django.contrib import admin
from .models import Service, Request

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']  # حسب الحقول يلي عندك

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'service', 'status', 'submitted_at']
    list_filter = ['status', 'service']
    search_fields = ['user__username', 'service__name']
