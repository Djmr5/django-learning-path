import decimal
from django.shortcuts import redirect, render
from .forms import Pago
from.models import Cliente

# Create your views here.
def procesador_de_pagos(request):
    if request.method == 'POST':
        form = Pago(request.POST)
        if form.is_valid():
            env = form.cleaned_data['envia']
            rec = form.cleaned_data['recibe']
            mon = decimal.Decimal(form.cleaned_data['monto'])
    else:
        form = Pago()
        return render(request, 'acid/index.html', {'form':form})
    
    envia_cliente = Cliente.objects.get(nombre = env)
    envia_cliente.saldo -= mon
    envia_cliente.save()

    recibe_cliente = Cliente.objects.get(nombre = rec)
    recibe_cliente.saldo += mon
    recibe_cliente.save()
    
    return redirect('/acid')