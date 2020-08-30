from django.db import models

# Create your models here.
class VideoUploader(models.Model):
    name = models.CharField(max_length=50)
    upload = models.FileField(upload_to="videos")

    def __str__(self):
        return self.name
    