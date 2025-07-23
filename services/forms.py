
# services/forms.py
from django import forms
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['service', 'full_name', 'national_id']
        widgets = {
            'service': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'full_name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'national_id': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
        }

