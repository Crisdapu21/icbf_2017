# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-10 23:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiario',
            name='grafica_peso',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='grafica_talla',
            field=models.TextField(blank=True),
        ),
    ]
