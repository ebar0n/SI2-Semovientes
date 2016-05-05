# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 04:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrativeunit',
            name='entity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='entities.Entity'),
            preserve_default=False,
        ),
    ]
