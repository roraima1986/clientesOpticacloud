from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
from .forms import *
from .models import *


class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/lista_cliente.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['create_url'] = reverse_lazy('nuevo_cliente')
        context['list_url'] = reverse_lazy('lista_clientes')
        context['total_opt_activas'] = Cliente.objects.filter(estado__contains='ACTIVA').count()
        context['total_plan_mensual'] = Cliente.objects.filter(estado__contains='ACTIVA', plan__contains='MENSUAL').count()
        context['total_plan_anual'] = Cliente.objects.filter(estado__contains='ACTIVA', plan__contains='ANUAL').count()
        return context


class ClienteCreateView(SuccessMessageMixin, CreateView):
    model = Cliente
    template_name = 'cliente/nuevo_cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('lista_cliente')
    success_message = "%(nombre_fantasia)s creado exitosamente"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Cliente'
        context['list_url'] = reverse_lazy('lista_cliente')
        return context


class ClienteUpdateView(SuccessMessageMixin, UpdateView):
    model = Cliente
    template_name = 'cliente/nuevo_cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('lista_cliente')
    success_message = "%(nombre_fantasia)s editado exitosamente"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Cliente'
        context['list_url'] = reverse_lazy('lista_cliente')
        return context


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente/detalle_cliente.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle Cliente'
        context['list_url'] = reverse_lazy('lista_cliente')
        return context
