from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'image_restore'
urlpatterns = [
                  # two paths: with or without given image
                  path('', views.index, name='restore'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.shortcuts import render

# Create your views here.
