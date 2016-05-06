from django.db import models


class Furnishing(models.Model):

    description = models.CharField(
        max_length=100,
        verbose_name="Descripcion (*)",
        help_text="Ingrese la descripcion del mueble"
    )

    year = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Año",
        help_text="Ingrese el año del mueble"
    )

    capacity = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Capacidad (*)",
        help_text="Ingrese la capacidad del mueble"
    )

    number_pieces = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Numero de piezas (*)",
        help_text="Ingrese la numero de piezas del mueble"
    )

    serial = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name="Serial (*)",
        help_text="Ingrese el serial del mueble"
    )

    license = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name="Placa (*)",
        help_text="Ingrese la placa del mueble"
    )

    height = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Altura (*)",
        help_text="Altura del mueble"
    )

    width = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Anchura (*)",
        help_text="Anchura del mueble"
    )

    length = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Longitud (*)",
        help_text="Longitud del mueble"
    )

    useful_life = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Vida util (*)",
        help_text="Vida util del mueble"
    )

    photo = models.ImageField(
        blank=True,
        null=True,
        upload_to='photos',
        verbose_name='Foto (*)',
        help_text='Ingrese la foto del mueble'
    )

    model = models.ForeignKey(
        'parameters.Model'
    )

    colour = models.ForeignKey(
        'parameters.Colour'
    )

    unit = models.ForeignKey(
        'parameters.MeasureUnit'
    )

    function = models.ForeignKey(
        'parameters.Function'
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
        verbose_name = 'Activo'
        verbose_name_plural = 'Activos'

    def __str__(self):
        return self.name


class Property(models.Model):

    description = models.CharField(
        max_length=100,
        verbose_name="Descripcion (*)",
        help_text="Ingrese la descripcion del inmueble"
    )

    function = models.ForeignKey(
        'parameters.Function'
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
        verbose_name = 'Inmueble'
        verbose_name_plural = 'Inmuebles'

    def __str__(self):
        return self.description


class Semoviente(models.Model):

    description = models.CharField(
        max_length=100,
        verbose_name="Descripcion (*)",
        help_text="Ingrese la descripcion del semoviente"
    )

    gender = models.ForeignKey(
        'parameters.Gender'
    )

    breed = models.ForeignKey(
        'parameters.Breed'
    )

    semoviente_suc = models.ForeignKey(
        'Semoviente'
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
        verbose_name = 'Semoviente'
        verbose_name_plural = 'Semovientes'

    def __str__(self):
        return self.description


class Catalog(models.Model):

    classification = models.CharField(
        max_length=100,
        verbose_name="Clasificacion (*)",
        help_text="Ingrese la Clasificacion"
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
        verbose_name = 'Catalogo'
        verbose_name_plural = 'Catalogos'

    def __str__(self):
        return self.name


class Assets(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Nombre (*)",
        help_text="Ingrese el nombre del activo"
    )

    correlative = models.CharField(
        unique=True,
        max_length=100,
        verbose_name="Correlativo (*)",
        help_text="Ingrese el correlativo del activo"
    )

    code = models.CharField(
        unique=True,
        max_length=100,
        verbose_name="Codigo (*)",
        help_text="Ingrese el codigo del activo"
    )

    furnishing = models.ForeignKey(
        'Furnishing'
    )

    property = models.ForeignKey(
        'Property'
    )

    semoviente = models.ForeignKey(
        'Semoviente'
    )

    catalog = models.ForeignKey(
        'Catalog'
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
        verbose_name = 'Activo'
        verbose_name_plural = 'Activos'

    def __str__(self):
        return self.name
