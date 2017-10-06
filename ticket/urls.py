"""ticket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from maintenance import views as maintenance
from barang import views as main
from chat import views as chat
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main.index, name='home'),
    url(r'^tes$', main.tes, name='tes'),
    url(r'^unit$', main.indexUnit, name='indexUnit'),
    url(r'^unit/add$', main.addUnit, name='addUnit'),
    url(r'^unit/edit/(?P<satuan_id>\d+)/$', main.editUnit, name='editUnit'),
    url(r'^unit/show/(?P<satuan_id>\d+)/$', main.showUnit, name='showUnit'),
    url(r'^unit/delete/(?P<satuan_id>\d+)/$', main.deleteUnit, name='deleteUnit'),
    
    url(r'^item$', main.indexItem, name='indexItem'),
    url(r'^item/add$', main.addItem, name='addItem'),
    url(r'^item/edit/(?P<barang_id>\d+)/$', main.editItem, name='editItem'),
    url(r'^item/show/(?P<barang_id>\d+)/$', main.showItem, name='showItem'),
    url(r'^item/delete/(?P<barang_id>\d+)/$', main.deleteItem, name='deleteItem'),
    
    url(r'^incoming$', main.indexIncoming, name='indexIncoming'),
    url(r'^incoming/add$', main.addIncoming, name='addIncoming'),
    url(r'^incoming/delete/(?P<incoming_id>\d+)/$', main.deleteIncoming, name='deleteIncoming'),
    #
    url(r'^repair$', maintenance.indexRepair, name='indexRepair'),
    url(r'^repair/add$', maintenance.addMaster, name='addRepair'),
    url(r'^repair/edit/(?P<id>\d+)/$', maintenance.editMaster, name='editRepair'),
    url(r'^repair/delete/(?P<repair_id>\d+)/$', maintenance.deleteRepair, name='deleteRepair'),

    url(r'^request$', maintenance.indexRequest, name='indexRequest'),
    url(r'^request/add$', maintenance.addRequest, name='addRequest'),
    url(r'^request/doit/(?P<request_id>\d+)/$',maintenance.doit,name='doit'),
    url(r'^request/finish/(?P<id>\d+)/$',maintenance.finishRequest,name='finish'),
    url(r'^request/view/(?P<request_id>\d+)/$', maintenance.viewRequest, name='viewRequest'),
    url(r'^createDetail$',maintenance.createDetail,name='createDetail'),
    url(r'^request/deleteItem/(?P<id>\d+)/$', maintenance.deleteItem, name='deleteItem'),
    url(r'^request/deleteDmaintenance/(?P<perbaikan_id>\d+)/$', maintenance.deleteDmaintenance, name='deleteDmaintenance'),

    url(r'^loan/',include('loan.urls')),
    url(r'^employee/',include('employee.urls')),

    url(r'^users/login/$', auth.login, {'template_name': 'login.html'}, name='login'),
    url(r'^users/logout/$', auth.logout, {'next_page': '/'}, name='logout'),
    url(r'^api/posts/',include("chat.api.urls",namespace='posts-api')),

    url(r'^chat/chat$',chat.addChat,name="chat"),
    url(r'^users/change_password/$', login_required(auth.password_change), {'post_change_redirect' : '/','template_name': 'change_password.html'}, name='change_password'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)