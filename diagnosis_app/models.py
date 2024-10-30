from django.db import models
from patients_app.models import Patients


class Diagnosis(models.Model):
    id = models.AutoField(primary_key=True)
    diagnosis_name = models.CharField(max_length=500)
    description = models.CharField(max_length=300)
    diagnosis_at = models.DateTimeField(auto_now_add=True)
    Patients_id = models.ForeignKey(Patients, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.diagnosis_name}"

