# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 03:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('regions', '0002_auto_20160504_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrativeUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ingrese el nombre de la unidad administrativa', max_length=100, verbose_name='Nombre (*)')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Unidad administrativa',
                'verbose_name_plural': 'Unidades administrativas',
            },
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ingrese el nombre de la entidad', max_length=100, verbose_name='Nombre (*)')),
                ('telephone', models.CharField(blank=True, help_text='Ingrese el telefóno de la entidad', max_length=12, null=True, verbose_name='Número Telefónico ')),
                ('fax', models.CharField(blank=True, help_text='Ingrese el fax de la entidad', max_length=12, null=True, verbose_name='Fax ')),
                ('email', models.EmailField(blank=True, help_text='Ingrese el correo electrónico', max_length=254, null=True, unique=True, verbose_name='Correo electrónico ')),
                ('address', models.CharField(blank=True, help_text='Ingrese la dirección de la entidad', max_length=150, null=True, verbose_name='Dirección ')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regions.Parish')),
            ],
            options={
                'verbose_name': 'Entidad',
                'verbose_name_plural': 'Entidades',
            },
        ),
    ]