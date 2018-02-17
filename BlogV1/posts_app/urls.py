from django.conf.urls import include, url
import views
from views import register_view ,login_view,logout_view

from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^home/$', views.home),
    url(r'^home/category/(?P<cat_id>[0-9]+)/$', views.category),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post),
    url(r'^register/$', register_view),
    url(r'^login/$', login_view),
    url(r'^logout/$' , logout_view) ,
    url(r'^commentreply/$', views.comment_reply)


]

