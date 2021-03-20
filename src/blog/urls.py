from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import index,blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog,name="blog"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, documents_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)