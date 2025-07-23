# users/forms.py
from django import forms
from .models import CitizenProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CitizenProfile
        fields = ['national_id', 'phone', 'address']