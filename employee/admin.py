# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Karyawan
class EmployeeAdmin(admin.ModelAdmin):
    class meta:
        model = Karyawan
    list_display = ('namaKaryawan','departemen','jabatan')

    # def Karyawan(self, obj):
    #     return obj.karyawan.namaKaryawan
    # def Departement(self,obj):
    #     return obj.karyawan.departemen
    # def User(self,obj):
    #     return obj.user.username
admin.site.register(Karyawan,EmployeeAdmin)
