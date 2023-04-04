from django.urls import path

from . views import *

urlpatterns = [
    path('', Index.as_view(), name='calculadora_index'),
    path('suma', Suma.as_view(), name='calculadora_suma'),
    path('resta', Resta.as_view(), name='calculadora_resta'),
    path('mult', Multiplicacion.as_view(), name='calculadora_multiplicacion'),
    path('div', Division.as_view(), name='calculadora_division')
]