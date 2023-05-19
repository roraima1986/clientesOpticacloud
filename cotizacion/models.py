from django.db import models
from cliente.models import Cliente


class Cotizacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name='Cliente')
    fecha = models.DateField(verbose_name='Fecha de Emisión')
    fecha_exp = models.DateField(verbose_name='Fecha de Expiración')
    plan = models.CharField(max_length=10, choices=[('MENSUAL', 'MENSUAL'), ('ANUAL', 'ANUAL')], verbose_name='Plan')
    tiendas = models.IntegerField(verbose_name='Tiendas', default=1)
    precio = models.IntegerField(verbose_name='Precio')
    subtotal = models.IntegerField(verbose_name='Sub-Total')
    iva_porcentaje = models.IntegerField(verbose_name='IVA(%)', default=19)
    iva_total = models.IntegerField(verbose_name='IVA Total')
    total = models.IntegerField(verbose_name='Total')
    creado = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    editado = models.DateTimeField(verbose_name='Editado', auto_now=True)

    def __str__(self):
        return self.cliente

    class Meta:
        verbose_name = 'Cotización'
        verbose_name_plural = 'Cotizaciones'
