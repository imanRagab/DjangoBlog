from django.conf.urls import include, url
import views
from views import register_view ,login_view

from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^home/$', views.home),
    url(r'^home/category/(?P<cat_id>[0-9]+)/$', views.category),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post),
    url(r'^register/$', register_view),
    url(r'^login/$', login_view),
    url(r'^commentreply/(?P<post_id>[0-9]+)/(?P<comment_id>[0-9]+)', views.comment_reply),
    url(r'^postcomment/(?P<post_id>[0-9]+)/$', views.post_comment),
    url(r'^likepost/$', views.like_post)

]

