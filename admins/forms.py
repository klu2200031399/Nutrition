# admins/forms.py
from django import forms
from Module.models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'phone_number', 'email', 'specialization', 'experience', 'password', 'salary']
