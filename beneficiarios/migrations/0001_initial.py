# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-29 19:59
from __future__ import unicode_literals

import beneficiarios.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entidad_administradora_servicio', '0001_initial'),
        ('parametrizacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, default=datetime.datetime.now)),
                ('tipo_beneficiario', models.CharField(max_length=2)),
                ('primer_nombre', models.TextField()),
                ('segundo_nombre', models.TextField(blank=True)),
                ('primer_apellido', models.TextField()),
                ('segundo_apellido', models.TextField(blank=True)),
                ('numero_documento', models.CharField(blank=True, max_length=15)),
                ('fecha_expedicion', models.CharField(blank=True, max_length=10)),
                ('lugar_expedicion', models.CharField(blank=True, max_length=5)),
                ('fecha_nacimiento', models.CharField(blank=True, max_length=10)),
                ('edad_anios', models.CharField(blank=True, max_length=2)),
                ('edad_meses', models.CharField(blank=True, max_length=2)),
                ('edad_anios_detalle', models.CharField(blank=True, max_length=4)),
                ('edad_meses_detalle', models.CharField(blank=True, max_length=5)),
                ('genero', models.CharField(max_length=1)),
                ('foto', models.ImageField(blank=True, upload_to=beneficiarios.models.beneficiario_directory_path)),
                ('grupo_etnico', models.CharField(blank=True, max_length=2)),
                ('grupo_perteneciente', models.TextField(blank=True)),
                ('a15', models.CharField(max_length=2)),
                ('a16', models.CharField(max_length=2)),
                ('direccion_acudiente', models.TextField(blank=True)),
                ('telefono_acudiente', models.CharField(blank=True, max_length=15, null=True)),
                ('a18', models.CharField(max_length=2)),
                ('a19', models.CharField(max_length=2)),
                ('modulo_b', models.CharField(blank=True, max_length=15)),
                ('modulo_c', models.CharField(blank=True, max_length=15)),
                ('modulo_d', models.CharField(blank=True, max_length=15)),
                ('modulo_e', models.CharField(blank=True, max_length=15)),
                ('modulo_f', models.CharField(blank=True, max_length=15)),
                ('modulo_g', models.CharField(blank=True, max_length=15)),
                ('a20', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Parentezco')),
                ('ciudad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Ciudades')),
                ('departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Departamentos')),
                ('pais', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Paises')),
                ('tipo_documento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Tipo_Documento')),
                ('uds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidad_administradora_servicio.UDS')),
            ],
            options={
                'verbose_name_plural': 'Crear Beneficiario',
            },
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uds', models.CharField(max_length=4)),
                ('fecha', models.DateField(blank=True, default=datetime.datetime.now)),
                ('hora', models.TimeField(blank=True, default=datetime.datetime.now)),
                ('nota', models.TextField()),
                ('beneficiario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='beneficiarios.Beneficiario')),
            ],
            options={
                'verbose_name_plural': 'Crear Notas del Beneficiario',
            },
        ),
    ]
