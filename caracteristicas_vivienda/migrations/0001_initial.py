# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-29 19:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('beneficiarios', '0001_initial'),
        ('parametrizacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaracteristicasVivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zona_ubicacion', models.CharField(max_length=2)),
                ('nombre_corregimiento', models.TextField(blank=True)),
                ('nombre_barrio', models.TextField(blank=True)),
                ('direccion_vivienda', models.TextField(blank=True)),
                ('tiempo_anios', models.CharField(blank=True, max_length=2, null=True)),
                ('tiempo_meses', models.CharField(blank=True, max_length=2, null=True)),
                ('b10', models.CharField(blank=True, max_length=2, null=True)),
                ('b11', models.CharField(blank=True, max_length=2)),
                ('b12', models.CharField(max_length=2)),
                ('b13', models.CharField(max_length=2)),
                ('b14', models.CharField(max_length=2)),
                ('b15', models.CharField(max_length=2)),
                ('b16_otro', models.TextField(blank=True)),
                ('b17_codigo', models.TextField(blank=True)),
                ('b17_nombre', models.TextField(blank=True)),
                ('b19_otro', models.TextField(blank=True)),
                ('b23', models.CharField(max_length=2)),
                ('b24_codigo', models.TextField(blank=True)),
                ('b24_nombre', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Crear Caracteristicas de Vivienda',
            },
        ),
        migrations.CreateModel(
            name='Fuente_Agua_Consumible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuente_agua_consumible', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Crear Fuentes de Agua Consumible',
            },
        ),
        migrations.CreateModel(
            name='Periodo_Agua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo_servicio_agua', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Crear Peridiocidad del Agua',
            },
        ),
        migrations.CreateModel(
            name='Servicios_Comunitarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Crear Servicios Comunitarios',
            },
        ),
        migrations.CreateModel(
            name='Servicios_Domiciliarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_servicio', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Crear Tipos de Servicio Domiciliario',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Cama',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_cama', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Crear Tipos de Cama',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Sanitario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_sanitario', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Crear Tipos de Sanitarios',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Tenencia_Vivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_tenencia_vivienda', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Crear Tipos de Tenencia de Vivienda',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Vivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_vivienda', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Crear Tipos de Vivienda',
            },
        ),
        migrations.CreateModel(
            name='Tratamiento_Basuras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tratamiento_basuras', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Crear Tipos de Tatamiento de Basuras',
            },
        ),
        migrations.CreateModel(
            name='Uso_Agua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uso_agua', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Crear Formas de uso del Agua',
            },
        ),
        migrations.AddField(
            model_name='caracteristicasvivienda',
            name='b16',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='caracteristicas_vivienda.Tipo_Cama'),
        ),
        migrations.AddField(
            model_name='caracteristicasvivienda',
            name='b18',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='caracteristicas_vivienda.Fuente_Agua_Consumible'),
        ),
        migrations.AddField(
            model_name='caracteristicasvivienda',
            name='b19',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='caracteristicas_vivienda.Periodo_Agua'),
        ),
        migrations.AddField(
            model_name='caracteristicasvivienda',
            name='b20',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='caracteristicas_vivienda.Uso_Agua'),
        ),
        migrations.AddField(
            model_name='caracteristicasvivienda',
            name='b21',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='caracteristicas_vivienda.Tratamiento_Basuras'),
        ),
        migrations.AddField(
            model_name='caracteristicasvivienda',
            name='b22',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='caracteristicas_vivienda.Tipo_Sanitario'),
        ),
        migrations.AddField(
            model_name='caracteristicasvivienda',
            name='beneficiario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beneficiarios.Beneficiario'),
        ),
        migrations.AddField(
            model_name='caracteristicasvivienda',
            name='ciudad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Ciudades'),
        ),
        migrations.AddField(
            model_name='caracteristicasvivienda',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Departamentos'),
        ),
        migrations.AddField(
            model_name='caracteristicasvivienda',
            name='pais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Paises'),
        ),
        migrations.AddField(
            model_name='caracteristicasvivienda',
            name='tipo_tenencia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='caracteristicas_vivienda.Tipo_Tenencia_Vivienda'),
        ),
        migrations.AddField(
            model_name='caracteristicasvivienda',
            name='tipo_vivienda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='caracteristicas_vivienda.Tipo_Vivienda'),
        ),
    ]
