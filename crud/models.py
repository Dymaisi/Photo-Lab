# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Member(models.Model):
    firstname = models.CharField(max_length=40, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    mobile_number = models.CharField(max_length=10, blank=True)
    description = models.TextField(max_length=255, blank=False)
    location = models.TextField(max_length=255, blank=False)
    date = models.DateField('%m/%d/%Y')
    created_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
    updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')

class ColorUpload(models.Model):
    user = models.CharField(max_length=40,default='123')
    photo = models.ImageField(upload_to='color_upload/', default='d.jpg')

class RestoreUpload(models.Model):
    user = models.CharField(max_length=40,default='123')
    photo = models.ImageField(upload_to='restore_upload/', default='d.jpg')

class StyleUpload(models.Model):
    user = models.CharField(max_length=40,default='123')
    photo = models.ImageField(upload_to='style_upload/', default='d.jpg')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class StyleImage(models.Model):
    style = models.CharField(max_length=40)
    img = models.ImageField(upload_to='styles/')




class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.CharField(max_length=255, )
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Ajax(models.Model):
    text = models.CharField(max_length=255, blank=True)
    search = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class CsvUpload(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    end_date = models.DateTimeField()
    notes = models.CharField(max_length=255, blank=True)
