from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service-list'),
    path('request/', views.service_request, name='service-request'),
    path('my-requests/', views.my_requests, name='my-requests'),
]
