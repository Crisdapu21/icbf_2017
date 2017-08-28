# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-27 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiario',
            name='edad',
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='edad_anios',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='edad_meses',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
