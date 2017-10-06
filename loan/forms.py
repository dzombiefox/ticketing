from django import forms
from .models import AsetBarang,PinjamBarang,PengembalianBarang

class AsetBarangForm(forms.ModelForm):
    class Meta:
        model=AsetBarang
        fields=['namaBarang','satuan','deskripsi','posted_by','status']

class PinjamBarangForm(forms.ModelForm):
    class Meta:
        model=PinjamBarang
        fields=['karyawan','keterangan','barang','return_plan','posted_by']

class  PengembalianBarangForm(forms.ModelForm):
    class Meta:
        model=PengembalianBarang
        fields=['pinjam','karyawan','keterangan']