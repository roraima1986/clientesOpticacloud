from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('lista_pago/', PagoListView.as_view(), name='lista_pago'),
    path('nuevo_pago/', PagoCreateView.as_view(), name='nuevo_pago'),
    path('editar_pago/<pk>/', PagoUpdateView.as_view(), name='editar_pago'),
    path('detalle_pago/<pk>/', PagoDetailView.as_view(), name='detalle_pago'),
    path('reporte_excel_pago/', views.reporte_excel_pago, name='reporte_excel_pago'),
]