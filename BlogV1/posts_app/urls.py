from django.conf.urls import include, url
import views

urlpatterns = [

    url(r'^post/(?P<post_id>[0-9]+)/$', views.post),

]