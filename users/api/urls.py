# users/api_urls.py
from django.urls import path
from .views import UserProfileView, UpdateUserProfileView

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='api-user-profile'),
    path('profile/update/', UpdateUserProfileView.as_view(), name='api-update-user-profile'),
]
