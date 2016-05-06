# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_auto_20160506_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='correlative',
            field=models.SlugField(
                editable=False, help_text='Ingrese el correlativo del activo', max_length=100,
                verbose_name='Correlativo (*)'),
        ),
        migrations.AlterField(
            model_name='purlieu',
            name='west',
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name='Oeste (*)'),
        ),
    ]
