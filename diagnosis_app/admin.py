from django.contrib import admin
from .models import Diagnosis


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('id', 'diagnosis_name', 'description', 'diagnosis_at', 'Patients_id')
