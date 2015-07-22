from django.conf.urls import url
from . import views

urlpatterns=[
url(r'^$',views.post_list,name='post_list'),
url(r'^post/(?P<pid>[0-9]+)/$', views.post_details, name='post_details'),
]