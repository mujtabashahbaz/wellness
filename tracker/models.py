from django.db import models
from django.contrib.auth.models import User

class WellnessLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()  # In minutes
    calories_burned = models.FloatField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity} on {self.date}"
