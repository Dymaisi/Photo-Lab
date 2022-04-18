import io
import os
import json
from io import BytesIO
from torchvision import models
from torchvision import transforms
from PIL import Image
from django.conf import settings
from .color import color_load_and_run
import cv2

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

def get_color_image(image_bytes):
    """For given image bytes, predict the label using the pretrained DenseNet"""
    output_image=color_load_and_run(image_bytes)
    return output_image


import base64
from django.shortcuts import render
from .forms import ImageUploadForm
from .models import Member
import time

def index(request):
    image_uri = None
    color_image_uri = None
    if request.method == 'POST':
        # in case of POST: get the uploaded image from the form and process it
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # retrieve the uploaded image and convert it to bytes (for PyTorch)
            image = form.cleaned_data['image']
            image_bytes = image.file.read()
            # convert and pass the image as base64 string to avoid storing it to DB or filesystem
            encoded_img = base64.b64encode(image_bytes).decode('ascii')
            image_url = os.path.join(os.path.join(BASE_DIR, 'media'), 'color_upload/%s.jpg' % int(
     time.strftime("%Y%m%d%H%M%S"))).replace(
     '\\', '/')
            image_uri = 'data:%s;base64,%s' % ('image/jpeg', encoded_img)
            with open(image_url, 'wb') as f:
                f.write(image_bytes)  # 打开路径将结果写入到文件中
                # 然后将图片路径保存到数据库
            # get predicted label with previously implemented PyTorch function
            try:
                output_image = get_color_image(image_bytes)
                encoded_img = base64.b64encode(output_image).decode('ascii')
                color_image_url = os.path.join(os.path.join(BASE_DIR, 'media'), 'color_img/%s.jpg' % int(
                    time.strftime("%Y%m%d%H%M%S"))).replace(
                    '\\', '/')
                with open(color_image_url, 'wb') as f:
                    f.write(output_image)  # 打开路径将结果写入到文件中
                color_image_uri = 'data:%s;base64,%s' % ('image/jpeg', encoded_img)
            except RuntimeError as re:
                print(re)

    else:
        # in case of GET: simply show the empty form for uploading images
        form = ImageUploadForm()

    # pass the form, image URI, and predicted label to the template to be rendered
    context = {
        'form': form,
        'image_uri': image_uri,
        'color_image_uri': color_image_uri,
    }
    return render(request, 'image_color/color.html', context)