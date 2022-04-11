from django.db import models

# Create your models here.
'''class RestoreImg(models.Model):
    user = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='restore_img/', default='avatar.jpg')'''


class RestoreUpload(models.Model):
    user = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='restore_upload/', default='avatar.jpg')