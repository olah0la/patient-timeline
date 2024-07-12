from django.contrib.auth.models import User
from django.db import models

class Patient(User):
    phone = models.CharField(max_length=20)
    address = models.TextField()
    birth_date = models.DateField()

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

class HealthProvider(User):
    phone = models.CharField(max_length=20)
    address = models.TextField()
    birth_date = models.DateField()
    specialty = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Health Provider'
        verbose_name_plural = 'Health Providers'

