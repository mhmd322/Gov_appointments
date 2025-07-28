from django.contrib import messages  

from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from services.models import User
from .forms import CustomRegisterForm
from users.models import CitizenProfile
from django.db import IntegrityError

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "تم تسجيل الخروج بنجاح.")
        return super().dispatch(request, *args, **kwargs)

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

def register_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            print("القيم المدخلة:")
            print("اسم المستخدم:", form.cleaned_data['username'])
            print("الرقم الوطني:", form.cleaned_data['national_id'])
            print("رقم الهاتف:", form.cleaned_data['phone'])
            print("العنوان:", form.cleaned_data['address'])

            user = form.save(commit=False)

            if User.objects.filter(username=form.cleaned_data['username']).exists():
                form.add_error('username', 'اسم المستخدم موجود بالفعل.')
                print("خطأ: اسم المستخدم موجود بالفعل.")
                return render(request, 'accounts/register.html', {'form': form})

            try:
                user.save()
                if CitizenProfile.objects.filter(national_id=form.cleaned_data['national_id']).exists():
                    form.add_error('national_id', 'الرقم الوطني مستخدم من قبل.')
                    print("خطأ: الرقم الوطني مستخدم من قبل.")
                    user.delete()
                    return render(request, 'accounts/register.html', {'form': form})

                CitizenProfile.objects.create(
                    user=user,
                    national_id=form.cleaned_data['national_id'],
                    phone=form.cleaned_data['phone'],
                    address=form.cleaned_data['address']
                )
                print(f"تم إنشاء المستخدم والبروفايل بنجاح: {user.username}")
                return redirect('login')
            except IntegrityError:
                form.add_error(None, "حدث خطأ أثناء التسجيل، حاول مرة أخرى.")
                print("IntegrityError: خطأ أثناء التسجيل.")
    else:
        form = CustomRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
