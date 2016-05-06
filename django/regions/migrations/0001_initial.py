# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 00:41
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Ciudades',
                'verbose_name': 'Cuidad',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Paises',
                'verbose_name': 'Pais',
            },
        ),
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='regions.Country')),
            ],
            options={
                'verbose_name_plural': 'Estados',
                'verbose_name': 'Estado',
            },
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='regions.City')),
            ],
            options={
                'verbose_name_plural': 'Municipios',
                'verbose_name': 'Municipio',
            },
        ),
        migrations.CreateModel(
            name='Parish',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('municipality', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='regions.Municipality')),
            ],
            options={
                'verbose_name_plural': 'Parroquias',
                'verbose_name': 'Parroquia',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='estate',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='regions.Estate'),
        ),
    ]
