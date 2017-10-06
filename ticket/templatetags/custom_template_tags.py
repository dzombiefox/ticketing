from django import template
from employee .models import Karyawan
from chat .models import Chat
register = template.Library()

@register.simple_tag
def get_rate():
    karyawan=Karyawan.objects.all()
    return karyawan

@register.simple_tag
def get_chat():
    chat=Chat.objects.all().order_by('-id')
    return chat