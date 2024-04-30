
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Profile
from django.contrib.auth.models import User,auth
from django.shortcuts import HttpResponse, redirect, render, get_object_or_404
from django.contrib import messages


def NewHomePage(request):
    return render(request, 'NewHomePage.html')


def Nutritiontip(request):
    return render(request, 'nutritiontips.html')

def pregnant(request):
    return render(request, 'pregnant.html')



def service(request):
    return render(request, 'service.html')


def articles(request):
    return render(request, 'articles.html')

def signup(request):
    return render(request, 'signup.html')



def login(request):
    return render(request, 'login.html')

def signup1(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1 != pass2:
            messages.error(request, 'Passwords do not match')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
        else:
            user = User.objects.create_user(username=username, email=email, password=pass1 )
            profile = Profile.objects.create(user=user)
            profile.save()
            messages.success(request, 'Account created successfully!!')
            return redirect('login')  # Redirect to login page after successful signup
    return render(request, 'signup.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('new_home')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login1')
        else:
            messages.error(request, 'Please provide both username and password')
            return redirect('login1')
    else:
        return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('/')


def About(request):
    return render(request, 'About us.html')


def recipe(request):
    return render(request, 'recipe.html')


def doctor_login(request):
    return HttpResponse("Doctor Login Page")


def admin_login(request):
    return HttpResponse("Admin Login Page")


def client_home(request):
    return render(request, 'client/home.html')


def doctor_home(request):
    return render(request, 'doctor/home.html')


def admin_home(request):
    return render(request, 'admins/home.html')


def home(request):
    return render(request, 'homepage.html')




def doclogin(request):
    return render(request, 'doctorlogin.html')
def doctorlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if Doctor.objects.filter(name=username,password=password).exists():
            return render(request,'doctor/base_doctor.html')
        else:
            return HttpResponse("Wrong Password")
    return render(request,'doctorlogin.html')


from .form import AppointmentForm
from .models import Doctor



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags

from .form import AppointmentForm


import stripe
from django.conf import settings

# Initialize Stripe with your secret key
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.username = request.user.username

            # Fetch user's phone number and email
            user_email = request.user.email

            # Save the appointment first
            appointment.save()

            # Create a payment intent with Stripe
            try:
                payment_intent = stripe.PaymentIntent.create(
                    amount=appointment.doctor.salary * 100,  # Convert to cents
                    currency='usd',
                    description='Appointment Payment',
                )

                return render(request, 'payment.html', {
                    'client_secret': payment_intent.client_secret,
                    'appointment': appointment,
                    'user_email': user_email,
                })
            except stripe.error.StripeError as e:
                # Handle any errors that occur during payment creation
                form.add_error(None, f"Payment failed: {e}")
    else:
        form = AppointmentForm()
    doctors_with_specialization = Doctor.objects.all().values_list('id', 'name', 'specialization')
    return render(request, 'book_appointment.html', {'form': form, 'doctors': doctors_with_specialization})

from .models import Appointment

def view_appointments(request):
    appointments = Appointment.objects.filter(username=request.user.username)
    return render(request, 'view_appointment.html', {'appointments': appointments})


@login_required
def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('view_appointments')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'edit_appointment.html', {'form': form})

@login_required
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('view_appointments')
    return render(request, 'delete_appointment.html', {'appointment': appointment})




def appointments(request):
    appointments = Appointment.objects.filter(username=request.user.username)
    return render(request, 'appointments.html', {'appointments': appointments})


from django.http import JsonResponse

def process_payment(request):
    # Retrieve payment method ID from POST data
    payment_method_id = request.POST.get('payment_method_id')

    try:
        # Confirm the payment with Stripe
        stripe.PaymentIntent.confirm(
            payment_method_id,
            amount=appointment.doctor.salary * 100,  # Convert to cents
            currency='usd',
            description='Appointment Payment',
        )
        # Payment succeeded
        return JsonResponse({'success': True})
    except stripe.error.StripeError as e:
        return JsonResponse({'success': False, 'error': str(e)})

def payment_success(request):
    return render(request, 'payment_success.html')

def payment_failure(request):
    return render(request, 'payment_failure.html')