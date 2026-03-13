
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('photo/<int:id>/', views.photoShow,name='photo'),
    path('cache/', views.my_cached_view, name='cache_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
