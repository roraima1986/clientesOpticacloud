from django.db import models
from cliente.models import Cliente

class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name='Cliente')
    concepto = models.CharField(max_length=200, verbose_name='Concepto', null=True, blank=True)
    fecha = models.DateField(verbose_name='Fecha')
    estado = models.CharField(max_length=10, choices=[('PENDIENTE', 'PENDIENTE'), ('LISTO', 'LISTO'), ('CANCELADO', 'CANCELADO')], verbose_name='Estado', default='PENDIENTE')
    creado = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    editado = models.DateTimeField(verbose_name='Editado', auto_now=True)

    def __str__(self):
        return self.cliente

    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Cita'