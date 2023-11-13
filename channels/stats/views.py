from django.shortcuts import render, redirect, get_object_or_404
from .models import Statistic, DataItem
from faker import Faker
from django.http import JsonResponse
from django.db.models import Sum

fake = Faker()

# Create your views here.
def main(request):
    qs = Statistic.objects.all()
    if request.method == 'POST':
        new_stat, _ = Statistic.objects.get_or_create(name=request.POST.get('new-statistic'))
        return redirect('stats:dashboard', slug=new_stat.slug)

    return render(request, 'stats/main.html', {'qs': qs})

def dashboard(request, slug):
    stat = get_object_or_404(Statistic, slug=slug)
    return render(request, 'stats/dashboard.html', {
        'name': stat.name,
        'slug': stat.slug,
        'data': stat.data,
        'user': request.user.username if request.user.username else fake.name(),
    })

def chart_data(request, slug):
    stat = get_object_or_404(Statistic, slug=slug)
    qs = stat.data.values('owner').annotate(Sum('value'))
    chart_data = [x['value__sum'] for x in qs]
    chart_labels = [x['owner'] for x in qs]
    return JsonResponse({
        'chartData': chart_data,
        'chartLabels': chart_labels,
    })