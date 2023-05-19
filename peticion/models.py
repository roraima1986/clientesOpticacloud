from django.db import models
from cliente.models import Cliente


class Peticion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name='Cliente')
    fecha = models.DateField(verbose_name='Fecha')
    peticion = models.CharField(max_length=200, verbose_name='Petición')
    estado = models.CharField(max_length=10, choices=[('PENDIENTE', 'PENDIENTE'), ('PROCESADA', 'PROCESADA')], verbose_name='Estado', default='PENDIENTE')
    observacion = models.CharField(max_length=200, verbose_name='Observación', null=True, blank=True)
    creado = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    editado = models.DateTimeField(verbose_name='Editado', auto_now=True)

    def __str__(self):
        return self.cliente

    class Meta:
        verbose_name = 'Petición'
        verbose_name_plural = 'Peticiones'
