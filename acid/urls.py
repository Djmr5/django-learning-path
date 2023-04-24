from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.procesador_de_pagos, name='transferencias')
]