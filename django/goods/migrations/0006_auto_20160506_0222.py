# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 06:52
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_auto_20160506_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='purlieu',
        ),
        migrations.AddField(
            model_name='purlieu',
            name='property',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='goods.Property'),
            preserve_default=False,
        ),
    ]