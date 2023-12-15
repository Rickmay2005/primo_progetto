from django.urls import path
from voti.views import lista_materie,voti_studenti,media_studenti,max_min_voti

app_name="voti"

urlpatterns = [
    path('lista_materie', lista_materie, name='lista_materie'),
    path('voti_studenti', voti_studenti, name='voti_studenti'),
    path('media_studenti', media_studenti, name='media_studenti'),
    path('max_min_voti', max_min_voti, name='max_min_voti'),
]
