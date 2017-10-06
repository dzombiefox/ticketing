from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from useremployee .models import UserEmployee
from .models import Barang,Satuan,BarangMasuk,Stok
from .forms import SatuanForm,BarangForm,BarangMasukForm
from django.http import HttpResponse
from django import template


@login_required
def index(request):
    current_user = request.user
    user=UserEmployee.objects.all()
    # return HttpResponse(user)
    return render(request, 'index.html',{"users":user})


def tes(request):
    return render(request, 'tes.html')

@login_required
def indexUnit(request):
    satuans=Satuan.objects.all()
    return render(request,'unit/index.html',{"satuans":satuans})

@login_required
def addItem(request):
    if request.POST:
        form=BarangForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/item/add",messages.success(request,'success add item','alert-success'))
            else:
                return redirect("/item/add",messages.error(request,'Data not Save','alert-danger'))
        else:
            return redirect("/item/add",messages.error(request,'Form is not Valid','alert-danger'))
    else :
        form = BarangForm()
        return render(request,'barang/add.html',{'form':form})

@login_required
def editUnit(request,satuan_id):
    satuan=Satuan.objects.get(id=satuan_id)
    if request.POST :
        form=SatuanForm(request.POST,instance=satuan)
        if form.is_valid():
            if form.save():
                return redirect("/unit",messages.success(request,'Success update Data','alert-success'))
            else :
                return redirect("/unit",messages.error(request,'Data not Saved','alert-danger'))
        else :
            return redirect ('/unit',messages.error(request,'Form is Not Valid','alert-danger'))
    else :
        form =SatuanForm(instance=satuan)
        return render(request,"unit/edit.html",{"form":form})



@login_required
def deleteUnit(request,satuan_id):
    satuan=Satuan.objects.get(id=satuan_id)
    satuan.delete()
    return redirect("/unit",messages.success(request,"Unit Was successfully deleted",'alert-success'))

@login_required
def showUnit(request,satuan_id):
    satuan=Satuan.objects.get(id=satuan_id)
    return render(request,"unit/show.html",{"satuan":satuan})


@login_required
def indexItem(request):
    barangs = Barang.objects.all()
    return render(request, 'barang/index.html', {"barangs": barangs})

@login_required
def addUnit(request):
    if request.POST:
        form=SatuanForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/unit/add",messages.success(request,'success add Unit','alert-success'))
            else :
                return redirect("/unit/add",messages.error(request,'Data is Not Save','alert-danger'))
        else :
            return redirect('/unit/add',messages.error(request,'Form is Not valid','alert-danger'))
    else :
        form =SatuanForm()
        return render(request,'unit/add.html',{'form':form})


@login_required
def deleteItem(request,barang_id):
    item=Barang.objects.get(id=barang_id)
    item.delete()
    return redirect("/item",messages.success(request,'Item Was successfully deleted','alert-success'))

@login_required
def editItem(request,barang_id):
    barang=Barang.objects.get(id=barang_id)
    if request.POST :
        form=BarangForm(request.POST,instance=barang)
        if form.is_valid():
            if form.save():
                return redirect("/item",messages.success(request,'Success Update Data','alert-success'))
            else :
                return redirect("/item",messages.error(request,'Data Not Update','alert-danger'))
        else:
            return redirect("/item",messages.error(request,'Form not Valid','alert-danger'))
    else :
        form=BarangForm(instance=barang)
        return render(request,"barang/edit.html",{"form":form})

@login_required
def showItem(request,barang_id):
    barang=Barang.objects.get(id=barang_id)
    return render(request,"barang/show.html",{"barang":barang})


@login_required
def indexIncoming(request):
    barangMasuk=BarangMasuk.objects.all()
    return render(request,'incoming/index.html',{"masuks":barangMasuk})


@login_required
def addIncoming(request):
    if request.POST:
        form = BarangMasukForm(request.POST)
        if form.is_valid():
            if form.save():
                barang = request.POST['barang']
                satuan = request.POST['satuan']
                qty = int(request.POST['quantity'])
                cekData = Stok.objects.filter(barang_id=barang, satuan_id=satuan)
                if cekData.exists():
                    data = Stok.objects.get(barang_id=barang, satuan_id=satuan)
                    Stok.objects.filter(pk=data.id).update(barang_id=barang, satuan_id=satuan,quantity=data.quantity + qty)
                else:
                    stok = Stok(barang_id=barang, satuan_id=satuan, quantity=qty)
                    stok.save()
                return redirect("/incoming",messages.success(request,'Success Save Data','alert-success'))
            else :
                return redirect("/incoming",messages.error(request,'Data Not Savee','alert-danger'))
        else:
            return redirect("/incoming",messages.error(request,'Form not Valid','alert-danger'))
    else :
        form =BarangMasukForm()
        return render(request,"incoming/add.html",{"form":form})


@login_required
def deleteIncoming(request,incoming_id):
    incoming=BarangMasuk.objects.get(id=incoming_id)
    # incoming.delete()
    qty=incoming.quantity
    satuan=incoming.satuan_id
    barang=incoming.barang_id
    data=Stok.objects.get(barang_id=barang,satuan_id=satuan)
    quantityStock=data.quantity
    valid=quantityStock-qty
    if valid < 0:
        return redirect("/incoming",messages.success(request, 'sory you cant deleted this Data , qty stock less than 0' , 'alert-success'))
    else :
        inc=BarangMasuk.objects.get(id=incoming_id)
        inc.delete()
        Stok.objects.filter(barang_id=barang,satuan_id=satuan).update(quantity=quantityStock-qty)
        return redirect("/incoming",messages.success(request,'Incoming Item Was successfully deleted','alert-success'))