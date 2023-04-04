from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request):
        return render(request, 'website/website_index.html')
    
class About(View):
    def get(self, request):
        return render(request, 'website/website_about.html')

class Content(View):
    def get(self, request):
        return render(request, 'website/website_content.html')