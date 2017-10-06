from django import forms
from .models import MasterPerbaikan,RequestPerbaikan,PemakaianBarang,DetailPerbaikan

class PerbaikanForm(forms.ModelForm):
    class Meta :
        model = MasterPerbaikan
        fields=['kodePerbaikan','namaPerbaikan','lamaPerbaikan','posted_by']

class RequestForm(forms.ModelForm):
    class Meta :
        model = RequestPerbaikan
        fields= ['permintaanPerbaikan','request','status']

class PemakaianBarangForm(forms.ModelForm):
    class Meta:
          model =PemakaianBarang
          fields=['id','barang','satuan','quantity','request','keterangan']

class DetailPerbaikanForm(forms.ModelForm):
    class Meta:
        model=DetailPerbaikan
        fields=['request','perbaikan']