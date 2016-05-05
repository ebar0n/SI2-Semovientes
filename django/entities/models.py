from django.db import models

# Create your models here.
class Entity(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Nombre (*)",
        help_text="Ingrese el nombre de la entidad"
    )

    telephone = models.CharField(
        max_length=12,
        verbose_name="Número Telefónico ",
        help_text="Ingrese el telefóno de la entidad",
        null=True,
        blank=True
    )

    fax = models.CharField(
        max_length = 12,
        verbose_name = "Fax ",
        help_text="Ingrese el fax de la entidad",
        null = True,
        blank = True
    )

    email = models.EmailField(
        unique=True,
        max_length=254,
        verbose_name="Correo electrónico ",
        help_text="Ingrese el correo electrónico",
        null=True,
        blank=True
    )

    parish = models.ForeignKey(
        'regions.Parish',
    )

    address = models.CharField(
        max_length=150,
        verbose_name="Dirección ",
        help_text="Ingrese la dirección de la entidad",
        null=True,
        blank=True
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
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'

    def __str__(self):
        return self.name


class AdministrativeUnit(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Nombre (*)",
        help_text="Ingrese el nombre de la unidad administrativa"
    )

    entity = models.ForeignKey(
        'Entity'
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
        verbose_name = 'Unidad administrativa'
        verbose_name_plural = 'Unidades administrativas'

    def __str__(self):
        return self.name