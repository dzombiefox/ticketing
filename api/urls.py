from django.conf.urls import url
from django.contrib import admin
from .views import (ChatSerializer)

urlpatterns=[
    url(r'^',ChatSerializer.as_view(),name='list')
]