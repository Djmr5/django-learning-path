from django.shortcuts import render
from django.views import View

from generic_views.models import Cat

# Create your views here.
class CatListView(View):
    def get(self, request):
        gatos = Cat.objects.all()
        context = {"lista_gatos":gatos}
        return render(request, 'generic_views/cat_list.html', context)

class CatDetailView(View):
    def get(self, request, cat_id):
        context = {
            "gato":Cat.objects.get(pk=cat_id)
        }
        return render(request, 'generic_views/cat_detail.html', context)
    
# Generic Views
from generic_views.models import Horse
from django.views import generic

class HorseListView(generic.ListView):
    model = Horse
    # generic views search for (class in lower case)_list.html

class HorseDetailView(generic.DetailView):
    model = Horse
    # generic views search for (class in lower case)details.html