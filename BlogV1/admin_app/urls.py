import views
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^allposts/$', views.allposts),
    url(r'^post_update/(?P<post_id>[0-9]+)/$', views.post_update),
    url(r'^post_create/$', views.post_create),
    url(r'^post_retrive/(?P<post_id>[0-9]+)/$', views.post_retrive),
    url(r'^post_delete/(?P<post_id>[0-9]+)/$', views.post_delete),
 #   url(r'^users/(?P<post_id>[0-9]+)/$', views.post_delete),
]
