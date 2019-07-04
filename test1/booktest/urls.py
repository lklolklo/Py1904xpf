#导入url函数
from django.conf.urls import url
#导入视图函数
# from .views import myviews
from . import views

app_name = "booktest"


urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^list/$',views.list,name="list"),
    url(r'^detail/(\d+)/$',views.detail,name="detail"),

    url(r'^addb/$',views.addb,name="addb"),
    url(r'^delb/(\d+)/$',views.delb,name="delb"),

    url(r'^addh/(\d+)/$',views.addh,name="addh"),
    url(r'^delt/(\d+)/$',views.delt,name="delt")
]