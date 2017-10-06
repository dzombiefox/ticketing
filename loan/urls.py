from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name="indexAset"),
	url(r'^addAsset',views.addAsset,name="addAset"),
	url(r'^editAset/(?P<id>\d+)$',views.editAset,name="editAset"),
  	url(r'^deleteAset/(?P<id>\d+)$',views.deleteAset,name="deleteAset"),
    url(r'^deleteBorrow/(?P<id>\d+)$',views.delBorrow,name="delBorrow"),
    url(r'^borrow',views.indexBorrow,name="indexBorrow"),
    url(r'^addBorrow',views.addBorrow,name="addBorrow"),
	url(r'^return', views.indexReturn, name="indexReturn"),
    url(r'^addReturn',views.addReturn,name="addReturn"),
    url(r'^deleteReturn/(?P<id>\d+)$',views.deleteReturn,name="deleteReturn"),

]
