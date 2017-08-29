# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-29 04:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parametrizacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entidad_Administradora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('numero_documento', models.CharField(max_length=15)),
                ('tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Tipo_Documento')),
            ],
            options={
                'verbose_name_plural': 'Crear Entidad Administradora',
            },
        ),
        migrations.CreateModel(
            name='Modalidades_servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modalidad', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Crear Modaliades del Servicio',
            },
        ),
        migrations.CreateModel(
            name='UDS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(blank=True)),
                ('direccion', models.TextField()),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Ciudades')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Departamentos')),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidad_administradora_servicio.Entidad_Administradora')),
                ('modalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidad_administradora_servicio.Modalidades_servicio')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Paises')),
            ],
            options={
                'verbose_name_plural': 'Crear UDS',
            },
        ),
    ]
