# Manassa/api_urls.py
from django.urls import path, include

urlpatterns = [
    path('appointments/', include('appointments.api.urls')),
    path('users/', include('users.api.urls')),
    path('services/', include('services.api.urls')),
    path('accounts/', include('accounts.api.urls')),
]
