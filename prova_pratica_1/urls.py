from django.urls import path
from prova_pratica_1.views import *

app_name="prova_pratica_1"
urlpatterns=[
    path('indexP', indexP, name='indexP'),
    path('somma', somma, name='somma'),
    path('media', media, name='media'),
    path('voti', voti, name='voti'),
]