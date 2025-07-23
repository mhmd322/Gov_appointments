from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .models import CitizenProfile, UserRole
from .forms import ProfileForm
from appointments.models import Appointment  

@login_required
def redirect_after_login(request):
    profile = request.user.citizenprofile
    if profile.role == UserRole.CITIZEN:
        return redirect('booking')
    elif profile.role == UserRole.EMPLOYEE:
        return redirect('employee-dashboard')
    elif profile.role == UserRole.ADMIN:
        return redirect('/admin/')
    return redirect('/')

class CustomLoginView(LoginView):
    def get_success_url(self):
        return '/users/redirect/'

@login_required
def profile_view(request):
    profile = request.user.citizenprofile
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
    profile = request.user.citizenprofile
    if profile.role != UserRole.EMPLOYEE:
        return redirect('/')

    appointments = Appointment.objects.select_related('user').all()
    return render(request, 'dashboard/employee_dashboard.html', {'appointments': appointments})

# users/views.py
# This view handles redirection after login based on user roles.
# It checks the user's profile and redirects to the appropriate page.
# If the user is a citizen, they are redirected to the booking page.
# If the user is an employee, they are redirected to the employee dashboard.
# If the user is an admin, they are redirected to the admin panel.
# If the user does not have a profile or role, they are redirected to the home page
# This view requires the user to be logged in, enforced by the @login_required decorator.
# The CustomLoginView class extends Django's LoginView to handle login functionality.       
# It overrides the get_success_url method to redirect users to the role-redirect URL after a successful login.
# This allows for a seamless user experience by directing users to the appropriate page based on their role immediately after logging in.
# This file is part of the users app, which manages user profiles and roles within the application.
# It imports necessary modules and decorators from Django, including render for rendering templates,
# redirect for URL redirection, and login_required to ensure that only authenticated users can access certain views.