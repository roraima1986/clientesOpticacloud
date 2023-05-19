from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
from .models import ProximoPago
from .forms import ProximoPagoForm


class ProximoPagoListView(ListView):
    model = ProximoPago
    template_name = 'proximo_pago/lista_proximo_pago.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Próximos Pagos'
        context['create_url'] = reverse_lazy('nuevo_proximo_pago')
        context['list_url'] = reverse_lazy('lista_proximo_pago')
        context['total_procesadas'] = ProximoPago.objects.filter(estado__contains='PROCESADA').count()
        context['total_pendientes'] = ProximoPago.objects.filter(estado__contains='PENDIENTE').count()
        context['total_canceladas'] = ProximoPago.objects.filter(estado__contains='CANCELADA').count()
        return context


class ProximoPagoCreateView(SuccessMessageMixin, CreateView):
    model = ProximoPago
    template_name = 'proximo_pago/nuevo_proximo_pago.html'
    form_class = ProximoPagoForm
    success_url = reverse_lazy('lista_proximo_pago')
    success_message = "%(cliente)s - %(fecha)s creado exitosamente"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Proximo Pago'
        context['list_url'] = reverse_lazy('lista_proximo_pago')
        return context


class ProximoPagoUpdateView(SuccessMessageMixin, UpdateView):
    model = ProximoPago
    template_name = 'proximo_pago/nuevo_proximo_pago.html'
    form_class = ProximoPagoForm
    success_url = reverse_lazy('lista_proximo_pago')
    success_message = "%(cliente)s - %(fecha)s editado exitosamente"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Proximo Pago'
        context['list_url'] = reverse_lazy('lista_proximo_pago')
        return context