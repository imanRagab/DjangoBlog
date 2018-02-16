from django.conf.urls import include, url
import views
from views import register_view ,login_view

urlpatterns = [

    url(r'^post/(?P<post_id>[0-9]+)/$', views.post),
    url(r'^register/$', register_view),
    url(r'^post/login/$', login_view),

]