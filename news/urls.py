from django.urls import path
from .views import home, articoloDetailView,listaArticoli,queryBase,giornalisti_list_api,giornalista_api,articolo_list_api,articolo_api

app_name="news"

urlpatterns=[
    path('', home, name="homeview"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articoli/<int:pk>", listaArticoli, name="lista_articoli_giornalista"),
    path("lista_articoli/", listaArticoli, name="lista_articoli"),
    path("query_base/", queryBase, name="query_base"),


    path('', home, name="homeview"),
    path("giornalisti_list_api/", giornalisti_list_api, name="giornalisti_list_api"),
    path("giornalista_api/<int:pk>", giornalista_api, name="giornalista_api"),
    path("articolo_list_api/", articolo_list_api, name="articolo_list_api"),
    path("articolo_api/<int:pk>", articolo_api, name="articolo_api")
]