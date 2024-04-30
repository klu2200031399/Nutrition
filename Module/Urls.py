from django.urls import path

from . import views
from .views import *

urlpatterns = [

    path('', home, name='home'),
    path('home/', NewHomePage, name='new_home'),
    path('Nutritiontip/',Nutritiontip,name='Nutritiontip'),
    path('service/',service,name='service'),
    path('articles/', articles, name='articles'),
    path('login/', login, name='login'),
    path('login1/', login1, name='login1'),
    path('signup/', signup, name='signup'),
    path('signup1/', signup1, name='signup1'),
    path('logout/', logout, name='logout'),
    path('About/', About, name="About"),
    path('recipe/', recipe, name='recipe'),
    path('login/doctor/', views.doctor_login, name='login_doctor'),
    path('login/admin/', views.admin_login, name='login_admin'),
    path('doclogin/',doclogin,name='doclogin'),
    path('doctorlogin/',doctorlogin,name='doctorlogin'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('view_appointments/', views.view_appointments, name='view_appointments'),
    path('pregnant/',pregnant,name='pregnant'),
    path('edit/<int:appointment_id>/', views.edit_appointment, name='edit_appointment'),
    path('delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('appointments/',views.appointments,name='appointments'),
path('process_payment/', views.process_payment, name='process_payment'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_failure/', views.payment_failure, name='payment_failure'),

]
