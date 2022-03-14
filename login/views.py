from django.shortcuts import render


def index(request):
    return render(request, 'index/index.html')


def enter(request):
    return render(request, 'index/option.html')


def sign(request):
    return render(request, 'index/sign_in.html')