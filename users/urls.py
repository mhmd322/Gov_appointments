from django.urls import path
from accounts.views import CustomLoginView  # استيراد من حسابات
from .views import redirect_after_login, profile_view, employee_dashboard
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('redirect/', redirect_after_login, name='role-redirect'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', profile_view, name='profile'),
    path('dashboard/', employee_dashboard, name='employee-dashboard'),
]
