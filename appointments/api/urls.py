# appointments/api_urls.py
from django.urls import path
from .views import (
    BookAppointmentView, MyAppointmentsView,
    EmployeeAppointmentsView, ConfirmAppointmentView,
    AdminAppointmentsView, EditAppointmentView
)

urlpatterns = [
    path('book/', BookAppointmentView.as_view(), name='api-book-appointment'),
    path('my/', MyAppointmentsView.as_view(), name='api-my-appointments'),
    path('employee/', EmployeeAppointmentsView.as_view(), name='api-employee-appointments'),
    path('employee/<int:appointment_id>/confirm/', ConfirmAppointmentView.as_view(), name='api-confirm-appointment'),
    path('admin/', AdminAppointmentsView.as_view(), name='api-admin-appointments'),
    path('admin/<int:appointment_id>/edit/', EditAppointmentView.as_view(), name='api-edit-appointment'),
]