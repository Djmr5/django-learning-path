from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "gviews"

urlpatterns = [
    path('', TemplateView.as_view(template_name='generic_views/main.html'), name='index'),
    path('cats', views.CatListView.as_view(), name='cats'),
    path('cat/<int:cat_id>', views.CatDetailView.as_view(), name='cat'),
    path('horses', views.HorseListView.as_view(), name='horses'),
    path('horse/<int:pk>', views.HorseDetailView.as_view(), name='horse')
]