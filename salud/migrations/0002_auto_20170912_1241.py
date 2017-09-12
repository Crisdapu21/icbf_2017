# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-12 17:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salud',
            name='f10',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='salud',
            name='f3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.EPS'),
        ),
        migrations.AlterField(
            model_name='salud',
            name='f4',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='salud',
            name='f6',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salud',
            name='f7',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='salud',
            name='f8',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salud',
            name='f9',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='salud',
            name='id_f6',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='salud',
            name='id_f8',
            field=models.TextField(blank=True),
        ),
    ]