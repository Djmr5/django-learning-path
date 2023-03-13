from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Fracciones
from fractions import Fraction

# Create your views here.

class Index(View):
    def get(request):
        return render(request, 'calculadora/calculadora_index.html')

class Suma(View):
    
    def get(self, request):
        return render(request, 'calculadora/suma/sumar.html')

    def post(self, request):
        primerNum= request.POST["primer_numerador"]
        primerDen= request.POST["primer_denominador"]
        segundoNum = request.POST["segundo_numerador"]
        segundoDen = request.POST["segundo_denominador"]

        res = str(Fraction(int(primerNum), int(primerDen)) + Fraction(int(segundoNum), int(segundoDen)))

        if res.find('/') != -1: 
            res_Num = res.split('/')[0]
            res_Den = res.split('/')[1]
        else:
            res_Num = res
            res_Den = "1"

        resultados = {
            'res_num': res_Num,
            'res_den': res_Den
        }
        # return JsonResponse(resultados)
        return render(request, 'calculadora/suma/sumaRes.html', resultados)

class Resta(View):
    
    def get(self, request):
        return render(request, 'calculadora/resta/restar.html')

    def post(self, request):
        primerNum= request.POST["primer_numerador"]
        primerDen= request.POST["primer_denominador"]
        segundoNum = request.POST["segundo_numerador"]
        segundoDen = request.POST["segundo_denominador"]

        res = str(Fraction(int(primerNum), int(primerDen)) - Fraction(int(segundoNum), int(segundoDen)))

        if res.find('/') != -1: 
            res_Num = res.split('/')[0]
            res_Den = res.split('/')[1]
        else:
            res_Num = res
            res_Den = "1"

        resultados = {
            'res_num': res_Num,
            'res_den': res_Den
        }
        # return JsonResponse(resultados)
        return render(request, 'calculadora/resta/restaRes.html', resultados)

class Multiplicacion(View):
    
    def get(self, request):
        return render(request, 'calculadora/multiplicacion/multiplicar.html')

    def post(self, request):
        primerNum= request.POST["primer_numerador"]
        primerDen= request.POST["primer_denominador"]
        segundoNum = request.POST["segundo_numerador"]
        segundoDen = request.POST["segundo_denominador"]

        res = str(Fraction(int(primerNum), int(primerDen)) * Fraction(int(segundoNum), int(segundoDen)))

        if res.find('/') != -1: 
            res_Num = res.split('/')[0]
            res_Den = res.split('/')[1]
        else:
            res_Num = res
            res_Den = "1"

        resultados = {
            'res_num': res_Num,
            'res_den': res_Den
        }
        # return JsonResponse(resultados)
        return render(request, 'calculadora/multiplicacion/multRes.html', resultados)

class Division(View):
    
    def get(self, request):
        return render(request, 'calculadora/division/dividir.html')

    def post(self, request):
        primerNum= request.POST["primer_numerador"]
        primerDen= request.POST["primer_denominador"]
        segundoNum = request.POST["segundo_numerador"]
        segundoDen = request.POST["segundo_denominador"]

        res = str(Fraction(int(primerNum), int(primerDen)) / Fraction(int(segundoNum), int(segundoDen)))

        if res.find('/') != -1: 
            res_Num = res.split('/')[0]
            res_Den = res.split('/')[1]
        else:
            res_Num = res
            res_Den = "1"

        resultados = {
            'res_num': res_Num,
            'res_den': res_Den
        }
        # return JsonResponse(resultados)
        return render(request, 'calculadora/division/divRes.html', resultados)