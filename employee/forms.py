from django import forms
from .models import Karyawan

class KaryawanForm(forms.ModelForm):
    class Meta:
        model=Karyawan
        fields=["namaKaryawan","departemen","jabatan",'prof_pic']