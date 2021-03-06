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
        'parameters.Model',
        verbose_name='Modelo'
    )

    colour = models.ForeignKey(
        'parameters.Colour',
        verbose_name='Color'
    )

    unit = models.ForeignKey(
        'parameters.MeasureUnit',
        verbose_name='Unidad de medida'
    )

    function = models.ForeignKey(
        'parameters.Function',
        verbose_name='Uso'
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
        verbose_name = 'Mueble'
        verbose_name_plural = 'Muebles'

    def __str__(self):
        return self.description


class Property(models.Model):

    description = models.CharField(
        max_length=100,
        verbose_name="Descripcion (*)",
        help_text="Ingrese la descripcion del inmueble"
    )

    file_number = models.CharField(
        max_length=100,
        verbose_name="Numero de expediente (*)",
        help_text="Ingrese el numero de expediente"
    )

    registry_number = models.CharField(
        max_length=100,
        verbose_name="Numero de registro (*)",
        help_text="Ingrese el numero de registro"
    )

    folio_number = models.CharField(
        max_length=100,
        verbose_name="Numero de folio (*)",
        help_text="Ingrese el numero de folio"
    )

    registry_day = models.DateField(
        verbose_name="Fecha de registro(*)",
        help_text="Ingrese la fecha de registro"
    )

    registration_office = models.CharField(
        max_length=100,
        verbose_name="Oficina de registro (*)",
        help_text="Ingrese la oficina de registro"
    )

    protocol = models.CharField(
        max_length=100,
        verbose_name="Protocolo (*)",
        help_text="Ingrese el protocolo"
    )

    volume = models.CharField(
        max_length=100,
        verbose_name="Tomo (*)",
        help_text="Ingrese el tomo"
    )

    quarter = models.CharField(
        max_length=100,
        verbose_name="Trimestre (*)",
        help_text="Ingrese el trismetre"
    )

    down_payment = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Deposito de garantia (*)",
        help_text="Ingrese el deposito de garantia"
    )

    rent_amount = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Monto de alquiler (*)",
        help_text="Ingrese el monto de alquiler"
    )

    appraised_current = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Avaluo actual (*)",
        help_text="Ingrese el avaluo actual"
    )

    appraised_commision = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Avaluo comision (*)",
        help_text="Ingrese el avaluo de comision"
    )

    function = models.ForeignKey(
        'parameters.Function',
        verbose_name='Uso'
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


class Purlieu(models.Model):

    north = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Norte (*)",
    )

    south = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Sur (*)",
    )

    east = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Este (*)",
    )

    west = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Oeste (*)",
    )

    land_area = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Area del terreno (*)",
    )

    covered_area = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Area cubierta (*)",
    )

    built_area = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Area construida (*)",
    )

    total_area = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Area total (*)",
    )

    property = models.OneToOneField(
        'Property'
    )

    class Meta:
        verbose_name = 'Lindero'
        verbose_name_plural = 'Linderos'


class Semoviente(models.Model):

    description = models.CharField(
        max_length=100,
        verbose_name="Descripcion (*)",
        help_text="Ingrese la descripcion del semoviente"
    )

    birth_day = models.DateField(
        verbose_name="Fecha de nacimiento (*)",
        help_text="Ingrese la fecha de nacimiento"
    )

    birth_weight = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Peso de nacimiento (*)",
        help_text="Ingrese el peso de nacimiento"
    )

    birth_estimated_value = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Valor estimado de nacimiento (*)",
        help_text="Ingrese el valor estimado de nacimiento"
    )

    current_weight = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Peso actual (*)",
        help_text="Ingrese el peso actual"
    )

    acquisition_value = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Valor de adquisicion (*)",
        help_text="Ingrese el valor de adquisicion"
    )

    species = models.ForeignKey(
        'parameters.Species',
        verbose_name='Especie'
    )

    gender = models.ForeignKey(
        'parameters.Gender',
        verbose_name='Genero'
    )

    semoviente_suc = models.ForeignKey(
        'Semoviente',
        verbose_name='Semoviente madre',
        null=True,
        blank=True,
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

    origin = models.ForeignKey(
        'self', null=True, blank=True
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
        strs = ''
        name = self.classification
        while self.origin:
            strs = self.origin.classification + ' - ' + strs
            self = self.origin
        return strs + name


class Assets(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Nombre (*)",
        help_text="Ingrese el nombre del activo"
    )

    correlative = models.SlugField(
        max_length=100,
        verbose_name="Correlativo (*)",
        help_text="Ingrese el correlativo del activo",
        editable=False
    )

    code = models.CharField(
        max_length=100,
        verbose_name="Codigo alterno (*)",
        help_text="Ingrese el codigo del activo",
        blank=True,
    )

    administrative_unit = models.ForeignKey(
        'entities.AdministrativeUnit',
        verbose_name='Unidad Administrativa'
    )

    furnishing = models.OneToOneField(
        'Furnishing', null=True
    )

    property = models.OneToOneField(
        'Property', null=True
    )

    semoviente = models.OneToOneField(
        'Semoviente', null=True
    )

    catalog = models.ForeignKey(
        'Catalog',
        verbose_name='Catalogo'
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
