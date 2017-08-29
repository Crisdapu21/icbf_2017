# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-29 04:15
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
            name='Salud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(max_length=2)),
                ('f2', models.CharField(blank=True, max_length=2)),
                ('semana_nacimiento', models.CharField(blank=True, max_length=4)),
                ('tipo_parto', models.CharField(blank=True, max_length=2)),
                ('servicio_parto', models.CharField(blank=True, max_length=2)),
                ('f4', models.CharField(max_length=2)),
                ('vacunas_1', models.TextField(blank=True)),
                ('vacunas_2', models.TextField(blank=True)),
                ('vacunas_3', models.TextField(blank=True)),
                ('vacunas_4', models.TextField(blank=True)),
                ('vacunas_5', models.TextField(blank=True)),
                ('vacunas_6', models.TextField(blank=True)),
                ('vacunas_7', models.TextField(blank=True)),
                ('vacunas_8', models.TextField(blank=True)),
                ('f6', models.TextField()),
                ('id_f6', models.TextField()),
                ('f6_otro', models.CharField(blank=True, max_length=20)),
                ('f7', models.CharField(max_length=2)),
                ('f8', models.TextField()),
                ('id_f8', models.TextField()),
                ('f8_otro', models.CharField(blank=True, max_length=20)),
                ('f9', models.CharField(max_length=2)),
                ('f10', models.CharField(max_length=2)),
                ('beneficiario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beneficiarios.Beneficiario')),
                ('f3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.EPS')),
            ],
        ),
    ]
