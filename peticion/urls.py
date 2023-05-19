from django.urls import path
from .views import *

urlpatterns = [
    path('lista_peticion/', PeticionListView.as_view(), name='lista_peticion'),
    path('nuevo_peticion/', PeticionCreateView.as_view(), name='nuevo_peticion'),
    path('editar_peticion/<pk>/', PeticionUpdateView.as_view(), name='editar_peticion'),
]