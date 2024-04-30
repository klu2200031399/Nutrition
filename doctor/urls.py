from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('', views.home, name='home'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('view_appointments1/', views.view_appointments, name='view_appointments1'),
    path('profile/', views.doctor_profile, name='doctor_profile'),

]

