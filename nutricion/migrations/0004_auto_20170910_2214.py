# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-11 03:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutricion', '0003_auto_20170910_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controles',
            name='edad_anios',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='controles',
            name='edad_meses',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='controles',
            name='total_meses',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]