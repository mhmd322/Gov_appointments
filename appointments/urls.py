from django.urls import path
from .views import booking_view, user_appointments, employee_appointments, confirm_appointment, admin_appointments, edit_appointment
from appointments import views

urlpatterns = [
    path('booking/', booking_view, name='booking'),
    path('my_appointments/', user_appointments, name='my-appointments'),
    path('employee/', employee_appointments, name='employee-appointments'),
    path('employee/confirm/<int:appointment_id>/', confirm_appointment, name='confirm-appointment'),
    path('admin/appointments/', admin_appointments, name='admin-appointments'),
    path('admin/edit/<int:appointment_id>/', edit_appointment, name='edit-appointment'),
    path('employee/dashboard/', views.employee_dashboard, name='employee-dashboard'),
    # تأكيد الموعد:
    path('employee/confirm/<int:pk>/', views.confirm_appointment, name='confirm-appointment'),
    # تعديل الموعد:
    path('admin/statistics/', views.admin_stats, name='admin-stats'),

]

# This file defines the URL patterns for appointment-related views, such as booking an appointment and viewing user appointments.
# It includes the necessary imports and maps the views to their respective URLs.                
