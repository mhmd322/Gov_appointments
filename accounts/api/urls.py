# accounts/api/urls.py
from django.urls import path
from .views import APILoginView, APIRegisterView

urlpatterns = [
    # ✅ API endpoints
    path('api/login/', APILoginView.as_view(), name='api-login'),
    path('api/register/', APIRegisterView.as_view(), name='api-register'),
]