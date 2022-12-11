from django.urls import path

from src.portal.views import Dashboard

app_name = "portal"

urlpatterns = \
    [
        path('dashboard/', Dashboard.as_view(), name="dashboard")
    ]
