# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ChatForm
from .models import Chat
from django.core import serializers
from django.contrib.auth.decorators import login_required,permission_required
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
# Create your views here.
@login_required
def addChat(request):
    form =ChatForm(request.POST)

    # if form.is_valid():
    form.save()


    return HttpResponse("ok")
    #     return HttpResponse("ok")
    # else:
    #     return HttpResponse("no ok")
   # data = Chat.objects.all()
   #  data = serializers.serialize('xml', Chat.objects.all(), fields=('chat','karyawan.namaKaryawan'))
   #  return  HttpResponse(data,content_type="application/json")
    #data=serializers.serialize("json",Chat.objects.filter().values_list('karyawan__namaKaryawan').all())
    #return  HttpResponse(data)
   # return HttpResponse(Chat.objects.filter().values_list('karyawan__namaKaryawan').all(), content_type="application/json")
    #data=Chat.objects.select_related("namaKaryawan").all()
    # for data in data :
    #     karyawan=data.karyawan.namaKaryawan
    #     kar=serializers.serialize("json",karyawan)
    #     return HttpResponse(kar,content_type="application/json")

