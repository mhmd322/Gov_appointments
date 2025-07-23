# appointments/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .forms import AppointmentForm
from .models import Appointment
from users.models import UserRole
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def booking_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.success(request, '✅ تم إرسال الحجز بنجاح، بانتظار التأكيد.')
            return redirect('my-appointments')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/booking.html', {'form': form})

@login_required
def user_appointments(request):
    appointments = Appointment.objects.filter(user=request.user).order_by('-date')
    return render(request, 'appointments/my_appointments.html', {'appointments': appointments})

@login_required
def employee_appointments(request):
    profile = request.user.citizenprofile
    if profile.role != UserRole.EMPLOYEE:
        return redirect('/')
    appointments = Appointment.objects.all().order_by('-date')
    return render(request, 'appointments/employee_dashboard.html', {'appointments': appointments})

@login_required
def confirm_appointment(request, appointment_id):
    profile = request.user.citizenprofile
    if profile.role != UserRole.EMPLOYEE:
        return redirect('/')
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.confirmed = True
    appointment.save()
    messages.success(request, f"تم تأكيد الموعد للمستخدم {appointment.user.username} ✳️")
    return redirect('employee-appointments')

@login_required
def admin_appointments(request):
    profile = request.user.citizenprofile
    if profile.role != UserRole.ADMIN:
        return redirect('/')
    appointments = Appointment.objects.all().order_by('-date')
    return render(request, 'appointments/admin_dashboard.html', {'appointments': appointments})

@login_required
def edit_appointment(request, appointment_id):
    profile = request.user.citizenprofile
    if profile.role != UserRole.ADMIN:
        return redirect('/')
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, '✔️ تم تعديل بيانات الموعد بنجاح.')
            return redirect('admin-appointments')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/edit_appointment.html', {'form': form, 'appointment': appointment})

def is_employee(user):
    return user.groups.filter(name='موظف').exists() or user.is_staff

@user_passes_test(is_employee)
def employee_dashboard(request):
    appointments = Appointment.objects.select_related('user').order_by('-date', '-time')
    return render(request, 'appointments/employee_dashboard.html', {'appointments': appointments})



@staff_member_required
def admin_stats(request):
    from .models import Appointment
    total = Appointment.objects.count()
    confirmed = Appointment.objects.filter(confirmed=True).count()
    pending = Appointment.objects.filter(confirmed=False).count()
    return render(request, 'appointments/admin_stats.html', {
        'total': total,
        'confirmed': confirmed,
        'pending': pending
    })
