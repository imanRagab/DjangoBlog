from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [

    url(r'^admin/$', views.dashboard),
    url(r'^admin/all/(?P<model>[a-z]+)', views.all),
    url(r'^admin/add/(?P<model>[a-z]+)$', views.add),
    url(r'^admin/edit/(?P<model>[a-z]+)/(?P<object_id>[0-9]+)', views.edit),
    url(r'^admin/delete/(?P<model>[a-z]+)/(?P<object_id>[0-9]+)$', views.delete),
    url(r'^admin/user/block/(?P<user_id>[0-9]+)$', views.block_user),
    url(r'^admin/user/unblock/(?P<user_id>[0-9]+)$', views.unblock_user),
    url(r'^admin/user/makeadmin/(?P<user_id>[0-9]+)$', views.make_admin),

]

# handler404 = 'posts_app.views.error_404'

