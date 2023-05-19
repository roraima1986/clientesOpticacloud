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
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concepto', models.CharField(blank=True, max_length=200, null=True, verbose_name='Concepto')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('estado', models.CharField(choices=[('PENDIENTE', 'PENDIENTE'), ('LISTO', 'LISTO'), ('CANCELADO', 'CANCELADO')], default='PENDIENTE', max_length=10, verbose_name='Estado')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('editado', models.DateTimeField(auto_now=True, verbose_name='Editado')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.cliente', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Cita',
                'verbose_name_plural': 'Cita',
            },
        ),
    ]
