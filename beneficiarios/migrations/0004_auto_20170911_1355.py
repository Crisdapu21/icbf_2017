# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-11 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiarios', '0003_auto_20170911_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiario',
            name='edad_anios',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='edad_meses',
            field=models.BigIntegerField(blank=True),
        ),
    ]