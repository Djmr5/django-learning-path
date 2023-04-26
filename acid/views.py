import decimal
from django.shortcuts import redirect, render
from .forms import Pago
from.models import Cliente
from django.contrib import messages
from django.db import transaction
import time

# Create your views here.
def procesador_de_pagos(request):
    # post request
    if request.method == 'POST':
        form = Pago(request.POST)
        if form.is_valid():
            env = form.cleaned_data['envia']
            rec = form.cleaned_data['recibe']
            mon = decimal.Decimal(form.cleaned_data['monto'])
        envia_cliente = Cliente.objects.select_for_update().get(nombre = env)
        recibe_cliente = Cliente.objects.select_for_update().get(nombre = rec)

        with transaction.atomic():
            envia_cliente.saldo -= mon
            envia_cliente.save()
            recibe_cliente.saldo += mon
            recibe_cliente.save()

        messages.success(request, "Transacción exitosa")
        
        return redirect('/acid')
    #get request
    else:
        form = Pago()
        return render(request, 'acid/index.html', {'form':form})