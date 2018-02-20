from django.conf.urls import include, url
from views import register_view ,login_view , like_view,unlike_view,dislike_view,undislike_view,search_view
from views import register_view ,login_view,logout_view
import views

# handler404 = 'posts_app.views.error_404'
urlpatterns = [
    url(r'^home/$', views.home),
    url(r'^home/category/(?P<cat_id>[0-9]+)/', views.category),
    url(r'^sup/(?P<cat_id>[0-9]+)/(?P<user_id>[0-9]+)/$', views.subscribe),
    url(r'^unsup/(?P<cat_id>[0-9]+)/(?P<user_id>[0-9]+)/$', views.unsubscribe),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post),
    url(r'^register/$', register_view),
    url(r'^login/$', login_view),
    url(r'^like/(?P<post_id>[0-9]+)/$', like_view),
    url(r'^unlike/(?P<post_id>[0-9]+)/$', unlike_view),
    url(r'^dislike/(?P<post_id>[0-9]+)/$', dislike_view),
    url(r'^undislike/(?P<post_id>[0-9]+)/$', undislike_view),
    url(r'^search/(?P<searchengine>[A-Za-z0-9]+)/$', search_view),
    url(r'^commentreply/$', views.comment_reply),
    url(r'^logout/$', views.logout_view),
    url(r'^commentreply/(?P<post_id>[0-9]+)/(?P<comment_id>[0-9]+)', views.comment_reply),
    url(r'^postcomment/(?P<post_id>[0-9]+)/$', views.post_comment),
    url(r'^likepost/$', views.like_post),
    #url(r'^issuped/(?P<cat_id>[0-9]+)/$', views.is_supped),


]




