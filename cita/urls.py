from django.urls import path
from .views import *

urlpatterns = [
    path('lista_cita/', CitaListView.as_view(), name='lista_cita'),
    path('nuevo_cita/', CitaCreateView.as_view(), name='nuevo_cita'),
    path('editar_cita/<pk>/', CitaUpdateView.as_view(), name='editar_cita')
]