from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"موعد {self.user.username} في {self.date} - {self.time}"