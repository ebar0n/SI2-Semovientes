# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 07:09
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='administrative_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to='entities.AdministrativeUnit', verbose_name='Unidad Administrativa'),
        ),
        migrations.AlterField(
            model_name='assets',
            name='catalog',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='goods.Catalog', verbose_name='Catalogo'),
        ),
        migrations.AlterField(
            model_name='furnishing',
            name='colour',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='parameters.Colour', verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='furnishing',
            name='function',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='parameters.Function', verbose_name='Uso'),
        ),
        migrations.AlterField(
            model_name='furnishing',
            name='model',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='parameters.Model', verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='furnishing',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to='parameters.MeasureUnit', verbose_name='Unidad de medida'),
        ),
        migrations.AlterField(
            model_name='property',
            name='function',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='parameters.Function', verbose_name='Uso'),
        ),
        migrations.AlterField(
            model_name='semoviente',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to='parameters.Gender', verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='semoviente',
            name='semoviente_suc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='goods.Semoviente', verbose_name='Semoviente madre'),
        ),
        migrations.AlterField(
            model_name='semoviente',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to='parameters.Species', verbose_name='Especie'),
        ),
    ]
