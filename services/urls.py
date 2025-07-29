from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service-list'),
    path('request/', views.service_request, name='service-request'),
    path('my-requests/', views.my_requests, name='my-requests'),
    path('employee/requests/', views.employee_requests_view, name='employee-requests'),
    path('employee/requests/<int:request_id>/update/', views.update_request_view, name='update-request'),

]