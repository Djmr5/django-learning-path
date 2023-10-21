from django.urls import path
from django.views.generic import TemplateView
from . views import *
from . import views

app_name = "website"

urlpatterns = [
    path('', TemplateView.as_view(template_name='website/website_index.html'), name='index'),
    path('about', TemplateView.as_view(template_name='website/website_about.html'), name='about'),
    path('content', views.content, name='content'),
    path('log', views.log, name='log'),
    path('crearAlumno', views.crearAlumno, name='crearAlumno')
]