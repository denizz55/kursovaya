from django.urls import path
from .views import *
from django.urls import path, include

urlpatterns = [
    path('', news, name = "news"),
    path('katalog/', katalog, name = "katalog"),
]