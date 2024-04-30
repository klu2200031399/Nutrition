from django.contrib.auth.backends import BaseBackend
from .models import Doctor

class DoctorAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            doctor = Doctor.objects.get(username=username)
            if doctor.check_password(password):
                return doctor
        except Doctor.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Doctor.objects.get(pk=user_id)
        except Doctor.DoesNotExist:
            return None
