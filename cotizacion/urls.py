from django.urls import path
from .views import *

urlpatterns = [
    path('lista_cotizacion/', CotizacionListView.as_view(), name='lista_cotizacion'),
    path('nuevo_cotizacion/', CotizacionCreateView.as_view(), name='nuevo_cotizacion'),
    path('editar_cotizacion/<pk>/', CotizacionUpdateView.as_view(), name='editar_cotizacion'),
    path('detalle_cotizacion/<pk>/', CotizacionDetailView.as_view(), name='detalle_cotizacion'),
]