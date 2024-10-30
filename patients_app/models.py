from django.db import models
from users_app.models import UserProfile


class Patients(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    symptoms = models.CharField(max_length=500)
    medical_history = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    userprofile_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name} - {self.symptoms}"

