from __future__ import unicode_literals
from django.db import models
from barang .models import Satuan
from django.contrib.auth.models import User
from employee .models import Karyawan

from django.db import models

# Create your models here.

class AsetBarang(models.Model):
      namaBarang=models.CharField(max_length=100)
      satuan=models.ForeignKey(Satuan)
      deskripsi=models.TextField(null=True)
      posted_by = models.ForeignKey(User)
      status=models.CharField(max_length=15)
      created_at = models.DateField(auto_now_add=True)
      updated_at = models.DateField(auto_now=True)

      def __str__(self):
            return self.namaBarang

class PinjamBarang(models.Model):
        karyawan=models.ForeignKey(Karyawan)
        keterangan=models.TextField(null=True)
        barang=models.ForeignKey(AsetBarang)
        return_plan = models.CharField(max_length=15)
        status=models.CharField(max_length=15,default=1)
        posted_by = models.ForeignKey(User)
        created_at = models.DateField(auto_now_add=True)
        updated_at = models.DateField(auto_now=True)


class PengembalianBarang(models.Model):
    karyawan=models.ForeignKey(Karyawan)
    pinjam=models.ForeignKey(PinjamBarang)
    keterangan = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
