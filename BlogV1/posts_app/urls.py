from django.conf.urls import include, url
import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^home/$', views.home),
    url(r'^home/category/(?P<cat_id>[0-9]+)/$', views.category),
    url(r'^sup/(?P<cat_id>[0-9]+)/(?P<user_id>[0-9]+)/$', views.subscribe),
    url(r'^unsup/(?P<cat_id>[0-9]+)/(?P<user_id>[0-9]+)/$', views.unsubscribe),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post),
    url(r'^register/$', views.register_view),
    url(r'^login/$', views.login_view),
    url(r'^logout/$', views.logout_view),
    url(r'^commentreply/(?P<post_id>[0-9]+)/(?P<comment_id>[0-9]+)', views.comment_reply),
    url(r'^postcomment/(?P<post_id>[0-9]+)/$', views.post_comment),
    url(r'^likepost/$', views.like_post),
    url(r'^issuped/(?P<cat_id>[0-9]+)/$', views.is_supped),

]

