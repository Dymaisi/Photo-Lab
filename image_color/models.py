from django.db import models

# Create your models here.
class ColorUpload(models.Model):
    user = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='color_upload/', default='avatar.jpg')