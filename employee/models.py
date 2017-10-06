# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Departemen(models.Model):
    namaDepartemen=models.CharField(max_length=25)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.namaDepartemen

class Jabatan(models.Model):
    namaJabatan=models.CharField(max_length=25)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.namaJabatan

class Karyawan(models.Model):
    namaKaryawan=models.CharField(max_length=50)
    departemen=models.ForeignKey(Departemen)
    jabatan=models.ForeignKey(Jabatan)
    prof_pic = models.ImageField("Photo Profile", upload_to='prof_pic/', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.namaKaryawan
