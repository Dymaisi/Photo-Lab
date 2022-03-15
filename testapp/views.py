from django.shortcuts import render
from . import models
from django.http import HttpResponse
# Create your views here.
def UpLoadInfo(request):
    if request.method == 'POST':
        image = models.Avatar(
            photo=request.FILES.get('photo'),
            user=request.FILES.get('photo').name
        )
        image.save()
        return HttpResponse('上传成功！')
    else:
        return render(request, 'testapp/test.html', locals())