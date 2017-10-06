# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.generics import ListAPIView
from chat.models import Chat
from .serializers import ChatSerializer
from django.shortcuts import render

# Create your views here.
class PostListApiView(ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer