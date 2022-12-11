
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core import settings

urlpatterns = \
    [
        path('admin/', admin.site.urls),
    ]

# Django Allauth Url

urlpatterns += \
    [
        path('accounts/', include('allauth.urls')),
    ]

# Application Urls

urlpatterns += \
    [

    ]
if settings.DEBUG:
    urlpatterns += [] + static(settings.MEDIA_URL, documents=settings.MEDIA_ROOT)
