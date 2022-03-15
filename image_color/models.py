from django.db import models

class Upload_Image(models.Model):
    user = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos', default='avatar.jpg')

# Create your models here.
