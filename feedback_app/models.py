from django.db import models
from users_app.models import UserProfile


class FeedBack(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    id = models.AutoField(primary_key=True)
    feedback = models.CharField(max_length=300)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    submitted_at = models.DateTimeField(auto_now_add=True)
    userprofile_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rating} - {self.userprofile.name} - {self.feedback}"




