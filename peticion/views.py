from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
from .forms import *
from .models import *


class PeticionListView(ListView):
    model = Peticion
    template_name = 'peticion/lista_peticion.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Peticiones'
        context['create_url'] = reverse_lazy('nuevo_peticion')
        context['list_url'] = reverse_lazy('lista_peticion')
        return context

class PeticionCreateView(SuccessMessageMixin, CreateView):
    model = Peticion
    template_name = 'peticion/nuevo_peticion.html'
    form_class = PeticionForm
    success_url = reverse_lazy('lista_peticion')
    success_message = "%(cliente)s creado exitosamente"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva Petición'
        context['list_url'] = reverse_lazy('lista_peticion')
        return context


class PeticionUpdateView(SuccessMessageMixin, UpdateView):
    model = Peticion
    template_name = 'peticion/nuevo_peticion.html'
    form_class = PeticionForm
    success_url = reverse_lazy('lista_peticion')
    success_message = "%(cliente)s editado exitosamente"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Petición'
        context['list_url'] = reverse_lazy('lista_peticion')
        return context