from django.shortcuts import render
from django.views import View

# Create your views here.
class ValidaUsuario(View):
    def get(self, request):
        return render(request, 'endpoints/validausuario.html')

    def post(self, request):
        user = request.POST["usuario"]
        password = request.POST["pass"]

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
        return render(request, 'endpoints/valida.html', resultados)