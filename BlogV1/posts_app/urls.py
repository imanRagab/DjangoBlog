from django.conf.urls import include, url
import views

urlpatterns = [

    url(r'^home/$', views.home),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post),

]