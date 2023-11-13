from django.urls import path
from .views import main, dashboard, chart_data

app_name = 'stats'

urlpatterns = [
    path('', main, name='main'),
    path('<str:slug>/', dashboard, name='dashboard'),
    path('<str:slug>/chart/', chart_data, name='chart'),
]