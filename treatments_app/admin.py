from django.contrib import admin
from .models import Treatments


@admin.register(Treatments)
class TreatmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'treatments_name', 'description', 'diagnosis_id')
