from rest_framework.generics import ListAPIView
from chat.models import Chat
from employee.models import Karyawan
from .serializers import ChatSerializer
from django.http import HttpResponse


class PostListApiView(ListAPIView):
    queryset = Chat.objects.all().order_by('-id')
    serializer_class = ChatSerializer

