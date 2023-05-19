# Generated by Django 4.1.4 on 2022-12-10 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de Emisión')),
                ('fecha_exp', models.DateField(verbose_name='Fecha de Expiración')),
                ('plan', models.CharField(choices=[('MENSUAL', 'MENSUAL'), ('ANUAL', 'ANUAL')], max_length=10, verbose_name='Plan')),
                ('tiendas', models.IntegerField(default=1, verbose_name='Tiendas')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('subtotal', models.IntegerField(verbose_name='Sub-Total')),
                ('iva_porcentaje', models.IntegerField(default=19, verbose_name='IVA(%)')),
                ('iva_total', models.IntegerField(verbose_name='IVA Total')),
                ('total', models.IntegerField(verbose_name='Total')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('editado', models.DateTimeField(auto_now=True, verbose_name='Editado')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.cliente', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Cotización',
                'verbose_name_plural': 'Cotizaciones',
            },
        ),
    ]
