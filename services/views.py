# services/views.py
from django.shortcuts import render, redirect
from .models import Service, Request
from .forms import RequestForm
from django.contrib.auth.decorators import login_required


def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})


@login_required
def service_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.user = request.user
            req.save()
            return redirect('my-requests')
    else:
        form = RequestForm()
    return render(request, 'services/service_request.html', {'form': form})


@login_required
def my_requests(request):
    requests = Request.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'services/my_requests.html', {'requests': requests})
