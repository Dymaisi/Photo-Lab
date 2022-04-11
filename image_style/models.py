from django.db import models

# Create your models here.
class StyleUpload(models.Model):
    user = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='style_upload/', default='avatar.jpg')