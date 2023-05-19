from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *
from .models import *
from .forms import *


class CitaListView(ListView):
    model = Cita
    template_name = 'cita/lista_cita.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Citas'
        context['create_url'] = reverse_lazy('nuevo_cita')
        context['list_url'] = reverse_lazy('lista_cita')
        return context


class CitaCreateView(SuccessMessageMixin, CreateView):
    model = Cita
    template_name = 'cita/nuevo_cita.html'
    form_class = CitaForm
    success_url = reverse_lazy('lista_cita')
    success_message = "%(cliente)s - %(fecha)s creado exitosamente"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva Cita'
        context['list_url'] = reverse_lazy('lista_cita')
        return context


class CitaUpdateView(SuccessMessageMixin, UpdateView):
    model = Cita
    template_name = 'cita/nuevo_cita.html'
    form_class = CitaForm
    success_url = reverse_lazy('lista_cita')
    success_message = "%(cliente)s - %(fecha)s editado exitosamente"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Cita'
        context['list_url'] = reverse_lazy('lista_cita')
        return context
