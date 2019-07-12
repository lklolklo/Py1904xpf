from . import views
from django.conf.urls import url

app_name = "comment"

urlpatterns = [
    url(r'^comment/(\d+)/$',views.AddComment.as_view(),name="comment")
]