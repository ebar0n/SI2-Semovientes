from django.db import models

# Create your models here.

class Function(models.Model):

    description = models.CharField(
        max_length=100,
        verbose_name="Funcion (*)",
        help_text="Ingrese la funcionalidad"
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
        verbose_name = 'Funcion'
        verbose_name_plural = 'Funciones'

    def __str__(self):
        return self.name


class Gender(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Nombre (*)",
        help_text="Ingrese el nombre del genero"
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
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'

    def __str__(self):
        return self.name


class Breed(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Nombre (*)",
        help_text="Ingrese el nombre de la raza"
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
        verbose_name = 'Raza'
        verbose_name_plural = 'Razas'

    def __str__(self):
        return self.name


class MeasureUnit(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Nombre (*)",
        help_text="Ingrese el nombre de la unidad de medida"
    )

    unit = models.CharField(
        max_length=10,
        verbose_name="Unidad (*)",
        help_text="Ingrese el simbolo de la unidad de medida"
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
        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'Unidades de medida'

    def __str__(self):
        return self.name


class Colour(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Nombre (*)",
        help_text="Ingrese el nombre del color"
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
        verbose_name = 'Color'
        verbose_name_plural = 'Colores'

    def __str__(self):
        return self.name


class Make(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Nombre (*)",
        help_text="Ingrese el nombre de la marca"
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
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.name


class Model(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Nombre (*)",
        help_text="Ingrese el nombre del modelo"
    )

    make = models.ForeignKey(
        'Make'
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
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'

    def __str__(self):
        return self.name
