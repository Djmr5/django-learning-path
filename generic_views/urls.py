from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "generic_views"

urlpatterns = [
    path('', TemplateView.as_view(template_name='generic_views/main.html')),
    path('cats', views.CatListView.as_view(), name='cats'),
    path('cat/<int:cat_id>', views.CatDetailView.as_view(), name='cat')
]