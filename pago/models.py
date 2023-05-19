from django.db import models
from cliente.models import Cliente


class Pago(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name='Cliente')
    mes = models.CharField(
        max_length=15,
        choices=[
            ('ENERO', 'ENERO'),
            ('FEBRERO', 'FEBRERO'),
            ('MARZO', 'MARZO'),
            ('ABRIL', 'ABRIL'),
            ('MAYO', 'MAYO'),
            ('JUNIO', 'JUNIO'),
            ('AGOSTO', 'AGOSTO'),
            ('SEPTIEMBRE', 'SEPTIEMBRE'),
            ('OCTUBRE', 'OCTUBRE'),
            ('NOVIEMBRE', 'NOVIEMBRE'),
            ('DICIEMBRE', 'DICIEMBRE'),
        ],
        verbose_name='Mes')
    year = models.IntegerField(verbose_name='Año')
    descripcion = models.CharField(max_length=200, verbose_name='Descripción', null=True, blank=True)
    cantidad = models.IntegerField(verbose_name='Tiendas', default=1)
    precio = models.IntegerField(verbose_name='Precio')
    subtotal = models.IntegerField(verbose_name='Sub-Total')
    iva_porcentaje = models.IntegerField(verbose_name='IVA(%)', default=19)
    iva_total = models.IntegerField(verbose_name='IVA Total')
    total = models.IntegerField(verbose_name='Total')
    n_factura = models.CharField(max_length=10, verbose_name='N° Factura (SII)', unique=True)
    fecha_factura = models.DateField(verbose_name='Fecha Factura (SII)')
    estado = models.CharField(max_length=10, choices=[('DEBE', 'DEBE'), ('PAGADA', 'PAGADA'), ('ANULADA', 'ANULADA')], verbose_name='Estado')
    fecha_pago = models.DateField(verbose_name='Fecha Pago', null=True, blank=True)
    observacion = models.CharField(max_length=200, verbose_name='Observación', null=True, blank=True)
    creado = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    editado = models.DateTimeField(verbose_name='Editado', auto_now=True)

    def __str__(self):
        return self.cliente

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'


