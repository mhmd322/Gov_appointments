# services/api_urls.py
from django.urls import path
from .views import (
    ServiceListView, SubmitRequestView,
    MyRequestsView, EmployeeRequestListView,
    UpdateRequestStatusView
)

urlpatterns = [
    path('', ServiceListView.as_view(), name='api-service-list'),
    path('request/', SubmitRequestView.as_view(), name='api-submit-request'),
    path('my/', MyRequestsView.as_view(), name='api-my-requests'),
    path('employee/', EmployeeRequestListView.as_view(), name='api-employee-requests'),
    path('employee/<int:request_id>/update/', UpdateRequestStatusView.as_view(), name='api-update-request-status'),
]