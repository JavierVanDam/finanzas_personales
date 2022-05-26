from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',
         include('rest_framework.urls')),  #esto es solo para el browsable api
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/', include('api.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),  # new

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
