from django.urls import path

from . views import *

urlpatterns = [
    path('', Index.as_view(), name='website_index'),
    path('about', About.as_view(), name='website_about'),
    path('content', Content.as_view(), name='website_content')
]