# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AsetBarangForm,PinjamBarangForm,PengembalianBarangForm
from .models import AsetBarang,PinjamBarang,PengembalianBarang
from django.db import models
# Create your views here.

@login_required
def index(request):
    data=AsetBarang.objects.all()
    return render(request,"aset/index.html",{"asets":data})

@login_required
def addAsset(request):
    if request.POST:
       form=AsetBarangForm(request.POST)
       if form.is_valid():
           if form.save():
               return redirect("/loan/addAsset", messages.success(request, 'success add asset', 'alert-success'))
           else :
               return redirect("/loan/addAsset", messages.error(request, 'Fail add asset', 'alert-error'))
       else :
           return redirect("/loan/addAsset", messages.error(request, 'Form fail !!', 'alert-error'))

    else:
        form=AsetBarangForm()
        return render(request,"aset/add.html",{"form":form})

@login_required
def editAset(request,id):
    aset = AsetBarang.objects.get(id=id)
    if request.POST:
        form=AsetBarangForm(request.POST,instance=aset)
        if form.is_valid():
            if form.save():
                return redirect("/loan",messages.success(request,"Success edit Data",'alert-success'))
            else :
                return redirect("/loan",messages.error(request,"Fail update data",'alert-error'))
        else :
            return request("/loan",messages.error(request,"Form Fail",'alert-error'))
    else :
        form=AsetBarangForm(instance=aset)
        return render(request,"aset/edit.html",{"form":form})


@login_required
def deleteAset(request,id):
    item=AsetBarang.objects.get(id=id)
    item.delete()
    return redirect("/loan", messages.success(request, 'Item Was successfully deleted', 'alert-success'))

@login_required
def indexBorrow(request):
    data=PinjamBarang.objects.all()
    return render(request,"loan/index.html",{"loan":data})

@login_required
def addBorrow(request):
    form=PinjamBarangForm(request.POST)
    if request.POST:
        # barang=AsetBarang.objects.get(request.POST['barang'])
        if form.is_valid():
            if form.save():
                AsetBarang.objects.filter(id=request.POST['barang']).update(status="used")
                return redirect("/loan/borrow",messages.success(request,"Loaning item successully added",'alert-success'))
            else :
                return redirect("/loan/borrow",messages.error(request,"Loaning item fail add"),'alert-error')
        else:
            return redirect("/loan/borrow", messages.error(request, "Form fail add"), 'alert-error')
    else :
        combo=AsetBarang.objects.filter(status="available")
        form=PinjamBarangForm()
        return render(request,"loan/add.html",{"form":form,"combo":combo})

@login_required
def delBorrow(request,id):
    borrow=PinjamBarang.objects.get(id=id)
    barang=borrow.barang_id
    AsetBarang.objects.filter(id=barang).update(status="available")
    borrow.delete()
    return redirect("/loan/borrow", messages.success(request, "Data Deleted..", 'alert-success'))

@login_required
def indexReturn(request):
    data=PengembalianBarang.objects.all();
    return render(request,"return/index.html",{"returns":data})

@login_required
def addReturn(request):
    if request.POST:
        form = PengembalianBarangForm(request.POST)
        if form.is_valid():
            if form.save():
                idpinjam=request.POST['pinjam']
                pinjam=PinjamBarang.objects.get(id=idpinjam)
                barang=pinjam.barang_id
                PinjamBarang.objects.filter(id=request.POST['pinjam']).update(status=2)
                AsetBarang.objects.filter(id=barang).update(status="available")
                return redirect("/loan/return",messages.success(request, "Data success added", 'alert-success'))
            else :
                return redirect("/loan/return", messages.error(request, "Data fail added", 'alert-error'))
        else :
            return redirect("/loan/return", messages.error(request, "Form Failed", 'alert-error'))
    else :
        form = PengembalianBarangForm()
        combo = PinjamBarang.objects.filter(status=1)
        return  render(request,"return/add.html",{"form":form,"combo":combo})

@login_required
def deleteReturn(request,id):
    returns=PengembalianBarang.objects.get(pk=id)
    PinjamBarang.objects.filter(id=returns.pinjam_id).update(status=1)
    AsetBarang.objects.filter(id=returns.pinjam.barang_id).update(status="used")
    returns.delete()
    return redirect("/loan/return", messages.success(request, "Data Deleted..", 'alert-success'))
   # return HttpResponse(returns.pinjam_id)
    #AsetBarang.objects.filter(id=barang).update(status="used")



