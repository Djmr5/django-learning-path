from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "generic_views"

urlpatterns = [
    path('', TemplateView.as_view(template_name='generic_views/main.html'), name='gviews_index'),
    path('cats', views.CatListView.as_view(), name='gviews_cats'),
    path('cat/<int:cat_id>', views.CatDetailView.as_view(), name='gviews_cat'),
    path('horses', views.HorseListView.as_view(), name='gviews_horses'),
    path('horse/<int:pk>', views.HorseDetailView.as_view(), name='gviews_horse')
]