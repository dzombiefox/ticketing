# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from employee .models import Karyawan

from django.db import models

# Create your models here.

class Chat(models.Model):
    chat=models.TextField()
    karyawan=models.ForeignKey(Karyawan, related_name='chats')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status=models.TextField(null=True)

    def __str__(self):
        return self.chat