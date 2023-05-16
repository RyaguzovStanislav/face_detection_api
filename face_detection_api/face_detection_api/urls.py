from api import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('upload_image/', views.upload_image, name='upload-image'),
    path('upload_image/detect/', views.detect_image, name='detection'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)