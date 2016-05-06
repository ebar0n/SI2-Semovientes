# -*- coding: utf-8 -*-
from django.db import models


class Country(models.Model):

    name = models.CharField(
        max_length=100
    )

    created_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.name


class Estate(models.Model):

    name = models.CharField(
        max_length=100
    )

    country = models.ForeignKey(
        'Country'
    )

    created_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.name


class City(models.Model):

    name = models.CharField(
        max_length=100
    )

    estate = models.ForeignKey(
        'Estate'
    )

    created_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    class Meta:
        verbose_name = 'Cuidad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return self.name


class Municipality(models.Model):

    name = models.CharField(
        max_length=100
    )

    city = models.ForeignKey(
        'City'
    )

    created_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return self.name


class Parish(models.Model):

    name = models.CharField(
        max_length=100
    )

    municipality = models.ForeignKey(
        'municipality'
    )

    created_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    class Meta:
        verbose_name = 'Parroquia'
        verbose_name_plural = 'Parroquias'

    def __str__(self):
        return self.name
