from django.urls import path
from .views import *

urlpatterns = [
    path('lista_proximo_pago/', ProximoPagoListView.as_view(), name='lista_proximo_pago'),
    path('nuevo_proximo_pago/', ProximoPagoCreateView.as_view(), name='nuevo_proximo_pago'),
    path('editar_proximo_pago/<pk>/', ProximoPagoUpdateView.as_view(), name='editar_proximo_pago')
]