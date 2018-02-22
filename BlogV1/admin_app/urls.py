from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [

    # url(r'^dashboard/$', views.dashboard),
    url(r'^$', views.allposts),
    url(r'^all/(?P<model>[a-z]+)', views.all),
    url(r'^add/(?P<model>[a-z]+)$', views.add),
    url(r'^edit/(?P<model>[a-z]+)/(?P<object_id>[0-9]+)$', views.edit),
    url(r'^delete/(?P<model>[a-z]+)/(?P<object_id>[0-9]+)$', views.delete),
    url(r'^user/block/(?P<user_id>[0-9]+)$', views.block_user),
    url(r'^user/unblock/(?P<user_id>[0-9]+)$', views.unblock_user),
    url(r'^user/makeadmin/(?P<user_id>[0-9]+)$', views.make_admin),

    url(r'^allposts/$', views.allposts),
    url(r'^post_update/(?P<post_id>[0-9]+)/$', views.post_update),
    url(r'^post_create/$', views.post_create),
    url(r'^post_retrive/(?P<post_id>[0-9]+)/$', views.post_retrive),
    url(r'^post_delete/(?P<post_id>[0-9]+)/$', views.post_delete),

    url(r'^allcategory/$', views.allcategory),
    url(r'^category_update/(?P<category_id>[0-9]+)/$', views.category_update),
    url(r'^category_create/$', views.category_create),
    url(r'^category_retrive/(?P<category_id>[0-9]+)/$', views.category_retrive),
    url(r'^category_delete/(?P<category_id>[0-9]+)/$', views.category_delete),

]

# handler404 = 'posts_app.views.error_404'

