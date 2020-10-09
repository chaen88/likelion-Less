from django.contrib import admin
from django.urls import path, include
from management import views
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('management.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)