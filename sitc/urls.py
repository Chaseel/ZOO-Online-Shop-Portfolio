from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from main.views import main, about_us


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='home'),
    path('products/', include('main.urls', namespace='products')),
    path('about_us/', about_us, name='about_us'),
    path('users/', include('users.urls', namespace='usesr')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)