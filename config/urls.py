from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('',include('news.urls')),
    path('admin_panel/',include('admin_panel.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
