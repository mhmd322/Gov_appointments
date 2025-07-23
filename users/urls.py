from django.urls import path
from .views import redirect_after_login, CustomLoginView, profile_view, employee_dashboard
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('redirect/', redirect_after_login, name='role-redirect'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', profile_view, name='profile'),
    path('dashboard/', employee_dashboard, name='employee-dashboard'),
]

# users/urls.py
# This file defines the URL patterns for user-related views, such as redirecting after login based