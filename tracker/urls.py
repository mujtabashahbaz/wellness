from django.urls import path
from .views import dashboard, log_activity, api_wellness_logs

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('log/', log_activity, name='log_activity'),
    path('api/wellness_logs/', api_wellness_logs, name='api_wellness_logs'),  # Add this line
]
