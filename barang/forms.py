from django import forms
from .models import Barang,Satuan,BarangMasuk

class SatuanForm(forms.ModelForm):
    class Meta :
        model = Satuan
        fields=['namaSatuan']
        
class BarangForm(forms.ModelForm):
    class Meta:
        model=Barang
        fields=['kodeBarang','namaBarang','satuan','posted_by']
class BarangMasukForm(forms.ModelForm):
    class Meta:
        model=BarangMasuk
        fields=['barang','satuan','quantity','keterangan','posted_by']


        