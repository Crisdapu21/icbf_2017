# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-12 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutricion', '0006_auto_20170910_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutricion',
            name='e11',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='nutricion',
            name='e3',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='nutricion',
            name='e5',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='nutricion',
            name='e6',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='nutricion',
            name='e7',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='nutricion',
            name='e9',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]