# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 05:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_assets_administrative_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.Catalog'),
        ),
    ]
