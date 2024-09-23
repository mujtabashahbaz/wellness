from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import WellnessLog
from .forms import WellnessLogForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import WellnessLogSerializer

@login_required
def dashboard(request):
    logs = WellnessLog.objects.filter(user=request.user)
    return render(request, 'tracker/dashboard.html', {'logs': logs})

@login_required
def log_activity(request):
    if request.method == 'POST':
        form = WellnessLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.save()
            return redirect('dashboard')
    else:
        form = WellnessLogForm()
    return render(request, 'tracker/log_activity.html', {'form': form})

@api_view(['GET'])
@login_required  # Ensure the user is logged in
def api_wellness_logs(request):
    logs = WellnessLog.objects.filter(user=request.user)
    serializer = WellnessLogSerializer(logs, many=True)
    return Response(serializer.data)
