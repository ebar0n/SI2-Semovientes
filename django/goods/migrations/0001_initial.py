# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 20:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parameters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ingrese el nombre del activo', max_length=100, verbose_name='Nombre (*)')),
                ('correlative', models.CharField(help_text='Ingrese el correlativo del activo', max_length=100, unique=True, verbose_name='Correlativo (*)')),
                ('code', models.CharField(help_text='Ingrese el codigo del activo', max_length=100, unique=True, verbose_name='Codigo (*)')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Activo',
                'verbose_name_plural': 'Activos',
            },
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.CharField(help_text='Ingrese la Clasificacion', max_length=100, verbose_name='Clasificacion (*)')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Catalogo',
                'verbose_name_plural': 'Catalogos',
            },
        ),
        migrations.CreateModel(
            name='Furnishing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='Ingrese la descripcion del mueble', max_length=100, verbose_name='Descripcion (*)')),
                ('year', models.IntegerField(blank=True, help_text='Ingrese el año del mueble', null=True, verbose_name='Año')),
                ('capacity', models.IntegerField(blank=True, help_text='Ingrese la capacidad del mueble', null=True, verbose_name='Capacidad (*)')),
                ('number_pieces', models.IntegerField(blank=True, help_text='Ingrese la numero de piezas del mueble', null=True, verbose_name='Numero de piezas (*)')),
                ('serial', models.CharField(blank=True, help_text='Ingrese el serial del mueble', max_length=100, null=True, verbose_name='Serial (*)')),
                ('license', models.CharField(blank=True, help_text='Ingrese la placa del mueble', max_length=100, null=True, verbose_name='Placa (*)')),
                ('height', models.IntegerField(blank=True, help_text='Altura del mueble', null=True, verbose_name='Altura (*)')),
                ('width', models.IntegerField(blank=True, help_text='Anchura del mueble', null=True, verbose_name='Anchura (*)')),
                ('length', models.IntegerField(blank=True, help_text='Longitud del mueble', null=True, verbose_name='Longitud (*)')),
                ('useful_life', models.IntegerField(blank=True, help_text='Vida util del mueble', null=True, verbose_name='Vida util (*)')),
                ('photo', models.ImageField(blank=True, help_text='Ingrese la foto del mueble', null=True, upload_to='photos', verbose_name='Foto (*)')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('colour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parameters.Colour')),
                ('function', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parameters.Function')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parameters.Model')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parameters.MeasureUnit')),
            ],
            options={
                'verbose_name': 'Activo',
                'verbose_name_plural': 'Activos',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='Ingrese la descripcion del inmueble', max_length=100, verbose_name='Descripcion (*)')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('function', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parameters.Function')),
            ],
            options={
                'verbose_name': 'Inmueble',
                'verbose_name_plural': 'Inmuebles',
            },
        ),
        migrations.CreateModel(
            name='Semoviente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='Ingrese la descripcion del semoviente', max_length=100, verbose_name='Descripcion (*)')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parameters.Breed')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parameters.Gender')),
                ('semoviente_suc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Semoviente')),
            ],
            options={
                'verbose_name': 'Semoviente',
                'verbose_name_plural': 'Semovientes',
            },
        ),
        migrations.AddField(
            model_name='assets',
            name='catalog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Catalog'),
        ),
        migrations.AddField(
            model_name='assets',
            name='furnishing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Furnishing'),
        ),
        migrations.AddField(
            model_name='assets',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Property'),
        ),
        migrations.AddField(
            model_name='assets',
            name='semoviente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Semoviente'),
        ),
    ]