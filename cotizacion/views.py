from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
from .forms import *
from .models import *


class CotizacionListView(ListView):
    model = Cotizacion
    template_name = 'cotizacion/lista_cotizacion.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Cotizaciones'
        context['create_url'] = reverse_lazy('nuevo_cotizacion')
        context['list_url'] = reverse_lazy('lista_cotizacion')
        return context


class CotizacionCreateView(SuccessMessageMixin, CreateView):
    model = Cotizacion
    template_name = 'cotizacion/nuevo_cotizacion.html'
    form_class = CotizacionForm
    success_url = reverse_lazy('lista_cotizacion')
    success_message = "%(cliente)s creado exitosamente"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva Cotización'
        context['list_url'] = reverse_lazy('lista_cotizacion')
        return context


class CotizacionUpdateView(SuccessMessageMixin, UpdateView):
    model = Cotizacion
    template_name = 'cotizacion/nuevo_cotizacion.html'
    form_class = CotizacionForm
    success_url = reverse_lazy('lista_cotizacion')
    success_message = "%(cliente)s creado exitosamente"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Cotización'
        context['list_url'] = reverse_lazy('lista_cotizacion')
        return context


class CotizacionDetailView(DetailView):
    model = Cotizacion
    template_name = 'cotizacion/detalle_cotizacion.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle Cotización'
        context['list_url'] = reverse_lazy('lista_cotizacion')
        return context