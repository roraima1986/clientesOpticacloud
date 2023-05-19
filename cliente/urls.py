from django.urls import path
from .views import *

urlpatterns = [
    path('lista_cliente/', ClienteListView.as_view(), name='lista_cliente'),
    path('nuevo_cliente/', ClienteCreateView.as_view(), name='nuevo_cliente'),
    path('editar_cliente/<pk>/', ClienteUpdateView.as_view(), name='editar_cliente'),
    path('detalle_cliente/<pk>/', ClienteDetailView.as_view(), name='detalle_cliente'),
    #path('delete_category/<pk>/', CategoryDeleteView.as_view(), name='delete_category'),

]