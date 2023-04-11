from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import Log, Alumno
from django.db.models import Max, Avg
from .forms import *

def content(request):
    
    maxp = Log.objects.all().aggregate(Max('points'))
    pointList = Log.objects.all().order_by('date')
    ctx = {'maxp': maxp["points__max"], "pointList" : pointList}
    return render(request, 'website/website_content.html', ctx)

def log(request):

    latest_logs = list(Log.objects.order_by('date').values())
    return JsonResponse(latest_logs, safe=False)

def crearAlumno(request):
    #POST
    if(request.method == 'POST'):
        form = AlumnoModelForm(request.POST)
        if(form.is_valid):
            form.save()
            request.session["msg"] = 'Nuevo Alumno creado: ' + form["nombre"].value()
            return redirect(request.path)
    #GET
    form = AlumnoModelForm
    msg = request.session.get('msj', False)
    if(msg): del(request.session['msj'])
    return render(request, 'website/crearAlumno.html', {'form':form, 'msj':msg})
        