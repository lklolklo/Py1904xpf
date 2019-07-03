#导入url函数
from django.conf.urls import url
#导入视图函数
# from .views import myviews
from . import views


urlpatterns = [
    url(r'^first/$',views.first),
    url(r'^seccend/$',views.seccend),
    url(r'^third/$',views.third)
]