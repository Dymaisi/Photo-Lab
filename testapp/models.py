from django.db import models

class Avatar(models.Model):
    user = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', default='avatar.jpg')