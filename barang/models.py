from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Satuan(models.Model):
    namaSatuan=models.CharField(max_length=15)

    def __str__(self):
        return self.namaSatuan

class Barang(models.Model):
    kodeBarang=models.CharField(max_length=15,verbose_name="KODE BARANG")
    namaBarang=models.CharField(max_length=45,verbose_name="NAMA BARANG")
    satuan=models.ForeignKey(Satuan,verbose_name="SATUAN")
    posted_by=models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return  self.namaBarang

class Stok(models.Model):
    barang=models.ForeignKey(Barang)
    satuan=models.ForeignKey(Satuan)
    quantity=models.IntegerField()

class BarangMasuk(models.Model):
      barang=models.ForeignKey(Barang)
      satuan=models.ForeignKey(Satuan)
      quantity=models.IntegerField()
      keterangan=models.TextField()
      posted_by = models.ForeignKey(User)
      created_at = models.DateField(auto_now_add=True)
      updated_at = models.DateField(auto_now=True)
