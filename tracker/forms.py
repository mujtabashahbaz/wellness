from django import forms
from .models import WellnessLog

class WellnessLogForm(forms.ModelForm):
    class Meta:
        model = WellnessLog
        fields = ['activity', 'duration', 'calories_burned', 'notes']
