from django.contrib import admin
from django.urls import path, include
from shop.views import home
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home)
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
