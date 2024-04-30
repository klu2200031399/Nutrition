# admins/views.py
from django.shortcuts import render, redirect
from .models import Doctor, Feedback
from .forms import DoctorForm


def admin_home(request):
    return render(request, 'admins/home.html')


def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admins:home')
    else:
        form = DoctorForm()

    return render(request, 'admins/add_doctor.html', {'form': form})


def view_feedbacks(request):
    feedbacks = Feedback.objects.all()
    context = {'feedbacks': feedbacks}
    return render(request, 'admins/view_feedbacks.html', context)


from django.shortcuts import render
from Module.models import Appointment

def view_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'admins/view_appointments.html', {'appointments': appointments})