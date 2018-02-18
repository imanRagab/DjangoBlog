from django.conf.urls import include, url
import views
from views import register_view ,login_view , like_view,unlike_view,dislike_view,undislike_view

from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^home/$', views.home),
    url(r'^home/category/(?P<cat_id>[0-9]+)/$', views.category),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post),
    url(r'^post/register/$', register_view),
    url(r'^post/login/$', login_view),
    url(r'^like/(?P<post_id>[0-9]+)/$', like_view),
    url(r'^unlike/(?P<post_id>[0-9]+)/$', unlike_view),
    url(r'^dislike/(?P<post_id>[0-9]+)/$', dislike_view),
    url(r'^undislike/(?P<post_id>[0-9]+)/$', undislike_view),
   # url(r'^search/$', search_view),
    url(r'^commentreply/$', views.comment_reply)

]

