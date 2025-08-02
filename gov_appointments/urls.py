# gov_appointments/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # المسارات العامة
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # مصادقة المستخدم عبر HTML
    path('accounts/', include('accounts.urls')),

    # API Djoser JWT
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # مسارات المستخدمين
    path('users/', include('users.urls')),

    # مسارات المواعيد
    path('appointments/', include('appointments.urls')),
    # مسارات الخدمات
    path('services/', include('services.urls')),
    
    # مسارات API
    path('api/', include('gov_appointments.api_urls')),
]
