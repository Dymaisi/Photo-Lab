from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'image_color'
urlpatterns = [
    # two paths: with or without given image
    path('', views.index, name='color'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)