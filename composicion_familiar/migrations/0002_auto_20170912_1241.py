# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-12 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('composicion_familiar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabeza_nucleo',
            name='c11',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='cabeza_nucleo',
            name='c3',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='cabeza_nucleo',
            name='c5',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='cabeza_nucleo',
            name='c6',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='cabeza_nucleo',
            name='c6_beneficio',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='cabeza_nucleo',
            name='c7',
            field=models.CharField(blank=True, max_length=1),
        ),
    ]
