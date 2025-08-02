# accounts/views.py
import traceback
from django.contrib import messages  
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.contrib.auth.models import User
from .forms import CustomRegisterForm
from users.models import CitizenProfile, UserRole  # تأكد من استيراد UserRole

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "تم تسجيل الخروج بنجاح.")
        return super().dispatch(request, *args, **kwargs)

def register_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            national_id = form.cleaned_data['national_id']
            phone = form.cleaned_data.get('phone', '')
            address = form.cleaned_data.get('address', '')

            # تحقق من وجود اسم مستخدم مسبقاً
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'اسم المستخدم موجود بالفعل.')
                return render(request, 'accounts/register.html', {'form': form})

            # تحقق من وجود رقم وطني مسبقاً
            if CitizenProfile.objects.filter(national_id=national_id).exists():
                form.add_error('national_id', 'الرقم الوطني مستخدم من قبل.')
                return render(request, 'accounts/register.html', {'form': form})

            try:
                # إنشاء المستخدم أولًا
                user = form.save(commit=False)
                user.save()

                # إنشاء بروفايل المواطن مع الدور citizen
                CitizenProfile.objects.create(
                    user=user,
                    role=UserRole.CITIZEN,
                    national_id=national_id,
                    phone=phone,
                    address=address,
                )

                messages.success(request, "تم إنشاء الحساب بنجاح، يمكنك تسجيل الدخول الآن.")
                return redirect('login')

            except IntegrityError:
                print(traceback.format_exc())
                form.add_error(None, "حدث خطأ أثناء التسجيل، حاول مرة أخرى.")
            except Exception:
                print(traceback.format_exc())
                form.add_error(None, "حدث خطأ غير متوقع أثناء التسجيل.")
        else:
            messages.error(request, "يرجى تصحيح الأخطاء في النموذج.")
    else:
        form = CustomRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})
