from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ourblog/', include('posts_app.urls')),
    url(r'^ourblog/', include('admin_app.urls')),
    url(r'^ourblog/', include('auth_app.urls')),
]

handler404 = 'posts_app.views.error_404'

if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
