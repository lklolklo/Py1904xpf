from django.conf.urls import url
from . import views

app_name = "shop"


urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^list/$',views.list,name="list"),
    url(r'^detail/$',views.detail,name="detail"),
    url(r'^login/$',views.login,name="login"),
    url(r'^register/$',views.register,name="register"),
    url(r'^logout/$',views.logout,name="logout"),
    url(r'^verify/$',views.verify,name="verify"),
    url(r'^active/(.*?)/$',views.active,name="active"),
]