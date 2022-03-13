import io
import os
import json
from io import BytesIO
from torchvision import models
from torchvision import transforms
from PIL import Image
from django.conf import settings
from .style import run_style_transfer
from .style import load_img

style='image_style/styles/ukiyoe.png'


def transform_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB').resize((512, 512))
    image = transforms.ToTensor()(image)
    image = image.unsqueeze(0)
    return image


def get_style_image(image_bytes):
    """For given image bytes, predict the label using the pretrained DenseNet"""
    image=transform_image(image_bytes)
    style_image=load_img(style)
    output_image = run_style_transfer(image,style_image,image,num_epoches=150)
    output_image = output_image.squeeze(0)
    output_image = transforms.ToPILImage()(output_image)
    new_img = output_image.convert("RGB")
    img_byte = BytesIO()
    new_img.save(img_byte, format='JPEG')  # format: PNG or JPEG
    output_image = img_byte.getvalue()  # im对象转为二进制流
    return output_image


import base64
from django.shortcuts import render
from .forms import ImageUploadForm


def index(request):
    image_uri = None
    style_image_uri = None

    if request.method == 'POST':
        # in case of POST: get the uploaded image from the form and process it
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # retrieve the uploaded image and convert it to bytes (for PyTorch)
            image = form.cleaned_data['image']
            image_bytes = image.file.read()
            # convert and pass the image as base64 string to avoid storing it to DB or filesystem
            encoded_img = base64.b64encode(image_bytes).decode('ascii')
            image_uri = 'data:%s;base64,%s' % ('image/jpeg', encoded_img)

            # get predicted label with previously implemented PyTorch function
            try:
                output_image = get_style_image(image_bytes)
                encoded_img = base64.b64encode(output_image).decode('ascii')
                style_image_uri = 'data:%s;base64,%s' % ('image/jpeg', encoded_img)
            except RuntimeError as re:
                print(re)

    else:
        # in case of GET: simply show the empty form for uploading images
        form = ImageUploadForm()

    # pass the form, image URI, and predicted label to the template to be rendered
    context = {
        'form': form,
        'image_uri': image_uri,
        'style_image_uri': style_image_uri,
    }
    return render(request, 'image_style/style_new.html', context)