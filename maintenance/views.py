# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import MasterPerbaikan,RequestPerbaikan,PemakaianBarang,DetailPerbaikan
from barang .models import Stok
from .forms import PerbaikanForm,RequestForm,PemakaianBarangForm,DetailPerbaikanForm
from django.shortcuts import render
from datetime import datetime
from django.http import  HttpResponse
# Create your views here.


@login_required
def indexRepair(request):
    master=MasterPerbaikan.objects.all()
    return render(request,'perbaikan/index.html',{"masters":master})

@login_required
def addMaster(request):
    if request.POST :
        form=PerbaikanForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/repair/add", messages.success(request, 'success add Data', 'alert-success'))
            else :
                return redirect("/repair/add",messages.error(request,'Fail add Data','alert-error'))
        else :
            return redirect("/repair/add",messages.error(request,"Form is Invalid"))
    else :
        form=PerbaikanForm()
        return render(request,"perbaikan/add.html",{"form":form })

@login_required
def editMaster(request,id):
    master = MasterPerbaikan.objects.get(pk=id)
    if request.POST:
        form=PerbaikanForm(request.POST,instance=master)
        if form.is_valid():
            if form.save():
                return redirect("/repair", messages.success(request, 'success Update Data', 'alert-success'))
            else:
                return redirect("/repair", messages.error(request, 'Fail add Data', 'alert-error'))
        else:
            return redirect("/repair", messages.error(request, "Form is Invalid"))
    else :
        form=PerbaikanForm(instance=master)
        return render(request,"perbaikan/edit.html",{"form":form})







@login_required
def deleteRepair(request,repair_id):
    item=MasterPerbaikan.objects.get(id=repair_id)
    item.delete()
    return redirect("/repair",messages.success(request,'Master Maintenance Was successfully deleted','alert-success'))

@login_required
def addRequest(request):
    if request.POST:
        form=RequestForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/request/add",messages.success(request,"success add Data",'alert-success'))
            else :
                return redirect("/request/add",messages.error(request,"Fail add Data"))
        else :
            return redirect("/request/add",messages.error(request,"Form is Invalid"))
    else :
        form=RequestForm()
        return render(request,"request/add.html",{"form":form})

@login_required
def indexRequest(request):
    current_user = request.user
    if request.user.is_superuser :
        requestPerbaikan = RequestPerbaikan.objects.all()
    else:
        requestPerbaikan = RequestPerbaikan.objects.filter(request=current_user.id)
    return  render(request,"request/index.html",{"datas":requestPerbaikan,"usr":request.user.is_superuser})

@login_required
def doit(request,request_id):
    user=request.user
    updateData=datetime.now()
    RequestPerbaikan.objects.filter(id=request_id).update(worked_by=user,worked_at=updateData,status='IN PROGRESS ...')
    return redirect("/request", messages.success(request, "Request In Progress..",'alert-success'))

@login_required
def viewRequest(request,request_id):
    if request.POST:
        form=PemakaianBarangForm(request.POST)
        if form.is_valid():
                barang = request.POST['barang']
                satuan = request.POST['satuan']
                qty = int(request.POST['quantity'])
                cekData = Stok.objects.filter(barang_id=barang, satuan_id=satuan)
                if cekData.exists():
                   data = Stok.objects.get(barang_id=barang, satuan_id=satuan)
                   quantity=data.quantity-qty
                   if quantity<0:
                       return redirect(request.META['HTTP_REFERER'],messages.error(request,"Quantity not enough"))
                   else:
                       Stok.objects.filter(pk=data.id).update(barang_id=barang, satuan_id=satuan,quantity=quantity)
                       form.save()
                       return redirect(request.META['HTTP_REFERER'])
                else :
                     return redirect(request.META['HTTP_REFERER'],messages.error(request,"Stok Not Found !! "))
        else :
            return redirect("/request", messages.error(request, "Form is invalid"))
    else :
        requestData=RequestPerbaikan.objects.get(id=request_id)
        detailBarang=PemakaianBarang.objects.filter(request_id=request_id)
        detailPerb=DetailPerbaikan.objects.filter(request_id=request_id)
        detail=PemakaianBarangForm()
        detailPerbaikan=DetailPerbaikanForm()
        return render(request,"request/view.html",{"form":requestData,"detail":detail,"barangs":detailBarang,"id":request_id,"detailForm":DetailPerbaikanForm,"perbaikans":detailPerb})

@login_required
def createDetail(request):
       if request.POST :
           form = DetailPerbaikanForm(request.POST)
           if form.is_valid():
               if form.save():
                   return redirect(request.META['HTTP_REFERER'])
               else :
                   return redirect(request.META['HTTP_REFERER'],messages.error(request,"Fail add data",'alert-error'))
           else :
               return redirect(request.META['HTTP_REFERER'],messages.error(request,"Form Error"),'alert-error')
       else :
            form =DetailPerbaikanForm()

@login_required
def deleteItem(request,id):
    data=PemakaianBarang.objects.get(id=id)
    barang=data.barang
    satuan=data.satuan
    quantity=data.quantity
    stok=Stok.objects.get(barang=barang,satuan=satuan)
    Stok.objects.filter(pk=stok.id).update(barang=barang, satuan=satuan, quantity=stok.quantity+quantity)
    data.delete()
    return redirect(request.META['HTTP_REFERER'])

@login_required
def deleteDmaintenance(request,perbaikan_id):
    item=DetailPerbaikan.objects.get(id=perbaikan_id)
    item.delete()
    return redirect(request.META['HTTP_REFERER'])

@login_required
def finishRequest(request,id):
    user = request.user
    updateData = datetime.now()
    RequestPerbaikan.objects.filter(id=id).update(finish_by=user, finish_at=updateData,status='FINISH')
    return redirect(request.META['HTTP_REFERER'])