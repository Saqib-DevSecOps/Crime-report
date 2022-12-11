from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView


# Create your views here.


@method_decorator(login_required,name='dispatch')
class Dashboard(TemplateView):
    template_name = 'portal/dashboard.html'
