from django.shortcuts import render
from django.views import View

from generic_views.models import Cat

# Create your views here.
class CatListView(View):
    def get(self, request):
        return render(request, 'generic_views/cat_list.html')

class CatDetailView(View):
    def get(self, request, cat_id):
        print(cat_id)
        ctx = {
            "id_cat":cat_id
        }
        return render(request, 'generic_views/cat_detail.html', ctx)