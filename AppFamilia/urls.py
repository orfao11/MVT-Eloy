from django.urls import path
from .views import *
urlpatterns = [
    path('', inicio, name="inicio"),
    path('familiarForm/', familiarForm, name= "familiarForm"),
    path('mascotaForm/', mascotaForm, name= "mascotaForm"),
    path('vecinoForm/', vecinoForm, name= "vecinoForm"),
    path('busquedaVecino/', busquedaVecino, name="busquedaVecino"),
    path('buscar/', buscar, name="buscar"),
]
