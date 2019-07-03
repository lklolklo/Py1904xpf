#导入url函数
from django.conf.urls import url
#导入视图函数
# from .views import myviews
from . import views


urlpatterns = [
    url(r'^$',views.index),
    url(r'^list/$',views.list),
    url(r'^detail/(\d+)/$',views.detail)
]