from django.conf.urls import url
from . import views

app_name = "votetest"


urlpatterns = [
    url(r'^$',views.list,name="list"),
    url(r'^answer/$',views.answer,name="answer"),
    url(r'^result/$',views.result,name="result"),
]