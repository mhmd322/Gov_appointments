# appointments/forms.py
from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'reason']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

class BookingForm(forms.Form):
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'w-full p-3 border border-gray-300 rounded-md shadow-sm'
        }),
        label="التاريخ"
    )
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'w-full p-3 border border-gray-300 rounded-md shadow-sm'
        }),
        label="الوقت"
    )
    reason = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3,
            'class': 'w-full p-3 border border-gray-300 rounded-md shadow-sm',
            'placeholder': 'اكتب سبب الحجز...'
        }),
        label="سبب الحجز"
    )