from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calc/', include('calculadora.urls')),
    path('polls/', include('polls.urls')),
    path('gviews/', include('generic_views.urls')),
    path('website/', include('website.urls')),
    path('admin/', admin.site.urls),
]