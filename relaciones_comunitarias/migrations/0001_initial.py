# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-30 08:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('beneficiarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d1', models.TextField()),
                ('id_d1', models.TextField()),
                ('d2', models.CharField(max_length=1)),
                ('d3', models.TextField()),
                ('id_d3', models.TextField()),
                ('d4', models.TextField()),
                ('id_d4', models.TextField()),
                ('d42', models.TextField()),
                ('id_d42', models.TextField()),
                ('d5', models.TextField()),
                ('id_d5', models.TextField()),
                ('d6', models.TextField()),
                ('id_d6', models.TextField()),
                ('d7', models.TextField()),
                ('id_d7', models.TextField()),
                ('d7_otro', models.CharField(blank=True, max_length=20)),
                ('d8', models.CharField(max_length=1)),
                ('d9', models.TextField()),
                ('id_d9', models.TextField()),
                ('beneficiario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beneficiarios.Beneficiario')),
            ],
            options={
                'verbose_name_plural': 'Crear Relaciones Comunitarias',
            },
        ),
    ]
