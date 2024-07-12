from django.contrib import admin
from .models import HealthProvider, Patient

@admin.register(HealthProvider)
class HealthProviderAdmin(admin.ModelAdmin):
    pass

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass
