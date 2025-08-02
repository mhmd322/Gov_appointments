# appointments/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AppointmentForm
from .models import Appointment
from users.models import UserRole

# ✅ دالة مساعدة لتحديد الدور
def get_user_role(user):
    try:
        return user.citizenprofile.role
    except:
        return None

# ✅ توجيه المستخدم بعد تسجيل الدخول حسب الدور
@login_required
def dashboard_redirect(request):
    role = get_user_role(request.user)
    if role == UserRole.EMPLOYEE:
        return redirect('employee-appointments')
    elif role == UserRole.ADMIN:
        return redirect('admin-appointments')
    else:
        return redirect('my-appointments')

# ✅ واجهة الحجز للمواطن
@login_required
def booking_view(request):
    if get_user_role(request.user) != UserRole.CITIZEN:
        return redirect('dashboard-redirect')

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

# ✅ مواعيدي (للمواطن)
@login_required
def user_appointments(request):
    if get_user_role(request.user) != UserRole.CITIZEN:
        return redirect('dashboard-redirect')

    appointments = Appointment.objects.filter(user=request.user).order_by('-date')
    return render(request, 'appointments/my_appointments.html', {'appointments': appointments})

# ✅ لوحة الموظف
@login_required
def employee_appointments(request):
    if get_user_role(request.user) != UserRole.EMPLOYEE:
        return redirect('dashboard-redirect')

    appointments = Appointment.objects.select_related('user').order_by('-date', '-time')
    return render(request, 'appointments/employee_dashboard.html', {'appointments': appointments})

# ✅ تأكيد الموعد (الموظف)
@login_required
def confirm_appointment(request, appointment_id):
    if get_user_role(request.user) != UserRole.EMPLOYEE:
        return redirect('dashboard-redirect')

    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.confirmed = True
    appointment.save()
    messages.success(request, f"✔️ تم تأكيد الموعد للمستخدم {appointment.user.username}")
    return redirect('employee-appointments')

# ✅ لوحة المشرف (المسؤول)
@login_required
def admin_appointments(request):
    if get_user_role(request.user) != UserRole.ADMIN:
        return redirect('dashboard-redirect')

    appointments = Appointment.objects.select_related('user').order_by('-date', '-time')
    return render(request, 'appointments/admin_dashboard.html', {'appointments': appointments})

# ✅ تعديل الموعد (المسؤول)
@login_required
def edit_appointment(request, appointment_id):
    if get_user_role(request.user) != UserRole.ADMIN:
        return redirect('dashboard-redirect')

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

# ✅ إحصائيات المشرف (المسؤول)
@login_required
def admin_stats(request):
    if get_user_role(request.user) != UserRole.ADMIN:
        return redirect('dashboard-redirect')

    total = Appointment.objects.count()
    confirmed = Appointment.objects.filter(confirmed=True).count()
    pending = Appointment.objects.filter(confirmed=False).count()

    return render(request, 'appointments/admin_stats.html', {
        'total': total,
        'confirmed': confirmed,
        'pending': pending
    })
employee_dashboard = employee_appointments
