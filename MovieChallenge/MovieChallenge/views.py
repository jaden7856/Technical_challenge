from django.views.generic import TemplateView, FormView
from django.shortcuts import render

class index(TemplateView):
    template_name = 'home.html'