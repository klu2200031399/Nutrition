# admins/urls.py
from django.urls import path
from . import views

app_name = 'admins'

urlpatterns = [
    path('', views.admin_home, name='home'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('view_feedbacks/', views.view_feedbacks, name='view_feedbacks'),
path('view-appointments/', views.view_appointments, name='view_appointments'),
    # Add more paths for other admin views as needed
]
