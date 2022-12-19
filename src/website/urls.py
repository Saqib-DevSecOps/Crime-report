from django.urls import path

from src.website.views import Home, Explore

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('explore/', Explore.as_view(), name="explore")
]
