from django.urls import path
from . views import *

app_name = "calculadora"

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('suma', Suma.as_view(), name='suma'),
    path('resta', Resta.as_view(), name='resta'),
    path('mult', Multiplicacion.as_view(), name='multiplicacion'),
    path('div', Division.as_view(), name='division')
]