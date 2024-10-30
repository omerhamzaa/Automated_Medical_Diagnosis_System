from django.db import models
from diagnosis_app.models import Diagnosis


class Treatments(models.Model):
    id = models.AutoField(primary_key=True)
    treatments_name = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    diagnosis_id = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)

    def __str__(self):
        return f"{{self.treatments_name}}"

