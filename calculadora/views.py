from django import forms
from django.shortcuts import render
from django.views import View

# Create your views here.

class Suma(View):
    
    def get(self, request):
        return render(request, 'calculadora/suma/sumar.html')

    def post(self, request):
        primerNum= request.POST["primer_numerador"]
        primerDen= request.POST["primer_denominador"]
        segundoNum = request.POST["segundo_numerador"]
        segundoDen = request.POST["segundo_denominador"]
        context = {}
        context['res_num'] = float(primerNum) + float(segundoNum)
        context['res_den'] = float(primerDen) + float(segundoDen)
        return render(request, 'calculadora/suma/sumaRes.html', context)

class Resta(View):
    
    def get(self, request):
        return render(request, 'calculadora/resta/restar.html')

    def post(self, request):
        return render(request, 'calculadora/resta/restaRes.html')

class Multiplicacion(View):
    
    def get(self, request):
        return render(request, 'calculadora/multiplicacion/multiplicar.html')

    def post(self, request):
        return render(request, 'calculadora/multiplicacion/multRes.html')

class Division(View):
    
    def get(self, request):
        return render(request, 'calculadora/division/dividir.html')

    def post(self, request):
        return render(request, 'calculadora/division/divRes.html')