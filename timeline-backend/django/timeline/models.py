from django.db import models
from main.models import Patient, HealthProvider

# Create your models here.
class Appointment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    paitient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    HealthProvider = models.ForeignKey(HealthProvider, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
