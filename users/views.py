# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .models import CitizenProfile, UserRole
from .forms import ProfileForm
from appointments.models import Appointment

@login_required
def redirect_after_login(request):
    user = request.user

    # إذا هو مسؤول (staff أو superuser)
    if user.is_staff or user.is_superuser:
        return redirect('/admin/')

    # جلب البروفايل إذا موجود
    profile = getattr(user, 'citizenprofile', None)
    if profile:
        if profile.role == UserRole.EMPLOYEE:
            return redirect('employee-dashboard')
        elif profile.role == UserRole.CITIZEN:
            return redirect('booking')

    # في حالة ما عنده بروفايل ولا هو مسؤول
    return redirect('home')


class CustomLoginView(LoginView):
    def get_success_url(self):
        return '/users/redirect/'


@login_required
def profile_view(request):
    profile = getattr(request.user, 'citizenprofile', None)
    if not profile:
        return redirect('home')

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/profile.html', {'form': form})


@login_required
def employee_dashboard(request):
    profile = getattr(request.user, 'citizenprofile', None)
    if not profile or profile.role != UserRole.EMPLOYEE:
        return redirect('home')

    appointments = Appointment.objects.select_related('user').all()
    return render(request, 'dashboard/employee_dashboard.html', {'appointments': appointments})
