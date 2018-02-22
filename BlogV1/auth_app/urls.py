from django.conf.urls import include, url
import views

# handler404 = 'posts_app.views.error_404'

urlpatterns = [

    url(r'^login/$', views.login_view),
    url(r'^register/$', views.register_view),
    url(r'^logout/$', views.logout_view),

]
