from django.contrib import admin
from .models import Patients


@admin.register(Patients)
class PatientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'symptoms', 'medical_history', 'created_at', 'updated_at', 'userprofile_id')
