import io
import os
import json
from io import BytesIO
from torchvision import models
from torchvision import transforms
from PIL import Image
from django.conf import settings
from django.shortcuts import render, redirect, HttpResponse
import datetime
from .restorage.run import run_cmd

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print(BASE_DIR)
def get_user_profiles(request):
  if request.method == 'POST':
    if request.FILES:
      myFile =None
      for i in request.FILES:
        myFile = request.FILES[i]
      if myFile:
        dir = os.path.join(BASE_DIR, 'media')
        dirupload = os.path.join(os.path.join(dir,'restore_upload'),'old_w_scratch')
        destination = open(os.path.join(dirupload, myFile.name),
                  'wb+')
        for chunk in myFile.chunks():
          destination.write(chunk)
        destination.close()
      return myFile.name



import base64
from django.shortcuts import render
from .forms import ImageUploadForm

def index(request):

    # pass the form, image URI, and predicted label to the template to be rendered
    image_uri = None
    restore_image_uri = None

    if request.method == 'POST':
        # in case of POST: get the uploaded image from the form and process it
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():

            # get predicted label with previously implemented PyTorch function
            try:
                file_name=get_user_profiles(request)
                dir = os.path.join(BASE_DIR, 'media')
                dirupload = os.path.join(os.path.join(dir, 'restore_upload'), 'old_w_scratch')
                dirout = os.path.join(os.path.join(dir, 'restore_img'),file_name)
                run_cmd(
                    "python image_restore/restorage/run.py --input_folder " + dirupload + " --output_folder " + dirout + " --GPU 0 --with_scratch")
                # upload_img = os.path.join(dirupload, file_name)
                # retore_img = os.path.join(os.path.join(dirout,'final_output'),file_name)
                form = ImageUploadForm()
                retore_img= 'restore_img/'+ file_name + '/final_output/'+file_name.split('.')[0]+'.png'
                upload_img = 'restore_upload/old_w_scratch/'+file_name


                restore_image_uri = retore_img
                image_uri= upload_img
            except RuntimeError as re:
                print(re)

    else:
        # in case of GET: simply show the empty form for uploading images
        form = ImageUploadForm()

    # pass the form, image URI, and predicted label to the template to be rendered
    context = {
        'form': form,
        'image_uri': image_uri,
        'restore_image_uri': restore_image_uri,
    }
    return render(request, 'image_restore/restore.html', context)