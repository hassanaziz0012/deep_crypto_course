from django.db import models
from django.utils import timezone


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=500)
    file = models.FileField(upload_to='videos')
    thumbnail = models.ImageField(upload_to='thumbnails')
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.title}"

    def __repr__(self) -> str:
        return f"<Video: {self.title}>"