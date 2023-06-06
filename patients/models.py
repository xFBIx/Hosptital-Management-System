from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, null=False)
    history_of_illness = models.TextField(null=True)
    record_of_prescriptions = models.TextField(null=True)

    def __str__(self):
        return f'{self.user.username} Patient Profile'
    
class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.CharField(max_length=100, null=False)
    service = models.CharField(max_length=100, null=False)
    health_issue = models.TextField(null=False)
    bill = models.IntegerField(null=False)
    bill_paid = models.BooleanField(default=False)
    date = models.DateField(null=False)
    time = models.TimeField(null=False)
    
    def __str__(self):
        return f'{self.patient.username} Appointment'
