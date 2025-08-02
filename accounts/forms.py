# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    national_id = forms.CharField(max_length=11, label="الرقم الوطني")
    phone = forms.CharField(max_length=14, label="رقم الهاتف")
    address = forms.CharField(max_length=255, label="العنوان")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "national_id", "phone", "address")
