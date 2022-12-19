from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class Home(TemplateView):
    template_name = "website/home.html"


class Explore(TemplateView):
    template_name = 'website/explore.html'
