# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import UserEmployee
class EmployeeAdmin(admin.ModelAdmin):
    class meta:
        model = UserEmployee
    list_display = ('Karyawan','User','Departement')

    def Karyawan(self, obj):
        return obj.karyawan.namaKaryawan
    def Departement(self,obj):
        return obj.karyawan.departemen
    def User(self,obj):
        return obj.user.username
admin.site.register(UserEmployee,EmployeeAdmin)
