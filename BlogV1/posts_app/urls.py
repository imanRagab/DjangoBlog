from django.conf.urls import include, url
import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^home/$', views.home),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post),
    url(r'^login/', auth_views.login, name='login')
]