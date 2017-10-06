from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$',views.index,name="indexEmployee"),
        url(r'^add',views.add,name="addEmployee"),
        url(r'^editEmployee/(?P<id>\d+)$',views.editEmployee,name="editEmployee"),
        url(r'^deleteEmployee/(?P<id>\d+)$',views.deleteEmployee,name="deleteEmployee"),


]