import datetime
from django.db import models

class Cliente(models.Model):
    razon_social = models.CharField(max_length=150, verbose_name='Razón Social')
    nombre_fantasia = models.CharField(max_length=150, verbose_name='Nombre de Fantasía')
    rut = models.CharField(max_length=12, verbose_name='Rut', unique=True)
    tiendas = models.IntegerField(verbose_name='Tiendas', default=1)
    correo = models.EmailField(verbose_name='Correo', null=True, blank=True)
    telefono = models.CharField(max_length=50, verbose_name='Teléfono', null=True, blank=True)
    direccion = models.CharField(max_length=200, verbose_name='Dirección',null=True, blank=True)
    ciudad = models.CharField(max_length=100, verbose_name='Ciudad',null=True, blank=True)
    comuna = models.CharField(max_length=100, verbose_name='Comuna',null=True, blank=True)
    contacto = models.CharField(max_length=100, verbose_name='Contacto', null=True, blank=True)
    telefono_contacto = models.CharField(max_length=50, verbose_name='Telefóno Contacto', null=True, blank=True)
    necesidad = models.CharField(max_length=200, verbose_name='Necesidad', null=True, blank=True)
    estado = models.CharField(max_length=15, choices=[('DEMO', 'DEMO'),('ACTIVA', 'ACTIVA'),('INHABILITADO', 'INHABILITADO')],
        verbose_name='Estado',null=True,blank=True)
    cuenta_demo = models.CharField(max_length=100, verbose_name='Cuenta Demo', null=True, blank=True)
    fecha_inicio_demo = models.DateField(verbose_name='Inicio Demo', null=True, blank=True)
    fecha_final_demo = models.DateField(verbose_name='Fin Demo', null=True, blank=True)
    cuenta_opticacloud = models.CharField(max_length=50, verbose_name='Cuenta OPTICACLOUD', null=True, blank=True)
    plan = models.CharField(max_length=10, choices=[('MENSUAL', 'MENSUAL'),('ANUAL', 'ANUAL')],
        verbose_name='Plan',null=True,blank=True)
    inicio_actividades = models.DateField(verbose_name='Inicio de Actividades', null=True, blank=True)
    fin_actividades = models.DateField(verbose_name='Fin de Actividades', null=True, blank=True)
    observacion = models.CharField(max_length=200, verbose_name='Observación', null=True, blank=True)
    creado = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    editado = models.DateTimeField(verbose_name='Editado', auto_now=True)

    def __str__(self):
        return self.nombre_fantasia

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
