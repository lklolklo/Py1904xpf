from django.conf.urls import url
from . import views

app_name = "votetest"


urlpatterns = [
    url(r'^$',views.list,name="list"),
    url(r'^answer/(\d+)/$',views.answer,name="answer"),
    url(r'^result/(\d+)/$',views.result,name="result"),
]