# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from barang.models import Barang,Satuan
from django.contrib.auth.models import User



# Create your models here.
class MasterPerbaikan(models.Model):
    kodePerbaikan=models.CharField(max_length=15)
    namaPerbaikan = models.CharField(max_length=105)
    lamaPerbaikan = models.CharField(max_length=45)
    posted_by = models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.namaPerbaikan

class RequestPerbaikan(models.Model):
    permintaanPerbaikan=models.TextField()
    request=models.ForeignKey(User,null=True,related_name="request")
    status=models.CharField(max_length=15, blank=True)
    worked_by=models.ForeignKey(User, null=True,related_name="worked_by")
    finish_by=models.ForeignKey(User,null=True,related_name="finish_by")
    worked_at=models.DateTimeField(null=True)
    finish_at=models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.permintaanPerbaikan

class PemakaianBarang(models.Model):
      barang =models.ForeignKey(Barang)
      satuan =models.ForeignKey(Satuan)
      quantity=models.IntegerField()
      request=models.ForeignKey(RequestPerbaikan)
      keterangan=models.TextField()
      created_at = models.DateField(auto_now_add=True)

class DetailPerbaikan(models.Model):
    perbaikan=models.ForeignKey(MasterPerbaikan)
    request=models.ForeignKey(RequestPerbaikan)

