from django.urls import path

from . views import *

urlpatterns = [
    path('', ValidaUsuario.as_view(), name='validausuario'),
]
