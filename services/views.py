# services/views.py
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect

from users.models import UserRole
from .models import Service, Request
from .forms import RequestForm
from django.contrib.auth.decorators import login_required


def service_list(request):
    q = request.GET.get('q', '')
    services = Service.objects.all()
    if q:
        services = services.filter(name__icontains=q)
    return render(request, 'services/service_list.html', {'services': services})

@login_required
def service_request(request):
    service_id = request.GET.get('service_id')
    initial_data = {}
    if service_id:
        initial_data['service'] = service_id

    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.user = request.user
            req.save()
            return redirect('my-requests')
    else:
        form = RequestForm(initial=initial_data)

    return render(request, 'services/service_request.html', {'form': form})


@login_required
def my_requests(request):
    requests = Request.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'services/my_requests.html', {'requests': requests})



@login_required
def employee_requests_view(request):
    profile = request.user.citizenprofile
    if profile.role != UserRole.EMPLOYEE:
        return redirect('/')

    requests_list = Request.objects.select_related('user', 'service').order_by('-submitted_at')
    return render(request, 'services/employee_requests.html', {'requests': requests_list})


@login_required
def update_request_view(request, request_id):
    profile = request.user.citizenprofile
    if profile.role != UserRole.EMPLOYEE:
        return redirect('/')

    req = get_object_or_404(Request, id=request_id)

    if request.method == 'POST':
        status = request.POST.get('status')
        valid_statuses = dict(Request._meta.get_field('status').choices).keys()
        if status in valid_statuses:
            req.status = status
            req.save()
            messages.success(request, f"✅ تم تحديث حالة الطلب إلى: {dict(Request._meta.get_field('status').choices)[status]}")
        else:
            messages.error(request, "❌ حالة غير صالحة")

    return redirect('employee-requests')