from django.urls import path
from .views import *


urlpatterns = [
    path('', news, name = "news"),
    path('katalog/', katalog, name = "katalog"),
    path('registration/', registration, name = "registration"),
    path('authorization/', authorization, name = "authorization"),
]