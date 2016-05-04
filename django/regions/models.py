# -*- coding: utf-8 -*-
from django.db import models


class Paises(models.Model):

    nombre = models.CharField(
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
        return self.nombre


class Estados(models.Model):

    nombre = models.CharField(
        max_length=100
    )

    pais = models.ForeignKey(
        'Paises'
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
        return self.nombre


class Ciudades(models.Model):

    nombre = models.CharField(
        max_length=100
    )

    estado = models.ForeignKey(
        'Estados'
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
        return self.nombre


class Municipios(models.Model):

    nombre = models.CharField(
        max_length=100
    )

    ciudad = models.ForeignKey(
        'Ciudades'
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
        return self.nombre


class Parroquias(models.Model):

    nombre = models.CharField(
        max_length=100
    )

    municipio = models.ForeignKey(
        'Municipios'
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
        return self.nombre