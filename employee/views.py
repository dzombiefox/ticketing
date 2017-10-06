from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import KaryawanForm
from .models import Karyawan
from django.db import models

# Create your views here.

@login_required
def index(request):
    data=Karyawan.objects.all()
    return  render(request,"karyawan/index.html",{"karyawans":data})

@login_required()
def add(request):
    if request.POST:
        form = KaryawanForm(request.POST,request.FILES)
        if form.is_valid():
            if form.save():
                return redirect("/employee/add",messages.success(request,"Success add employee",'message-success'))
            else :
                return redirect("/employee/add", messages.error(request, "Failed add employee", 'message-error'))
        else :
            return redirect("/employee/add", messages.error(request, "Form  Error", 'message-error'))
    else :
        form=KaryawanForm()
        return render(request,"karyawan/add.html",{"form":form})


@login_required
def deleteEmployee(request,id):
    employee=Karyawan.objects.get(id=id)
    employee.delete()
    return redirect("/employee",messages.success(request,"Success delete Employee",'alert-success'))

@login_required
def editEmployee(request,id):
    karyawan=Karyawan.objects.get(id=id)
    if request.POST:
       form=KaryawanForm(request.POST,request.FILES,instance=karyawan)
       if form.is_valid():
           if form.save():
               return redirect("/employee", messages.success(request, "Success Edit employee", 'message-success'))
           else:
               return redirect("/employee", messages.error(request, "Failed edit employee", 'message-error'))
       else:
           return redirect("/employee", messages.error(request, "Form  Error", 'message-error'))

    else :
       form=KaryawanForm(instance=karyawan)
       return render(request,"karyawan/edit.html",{"form":form})