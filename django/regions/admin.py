from django.contrib import admin

from regions import models


@admin.register(models.Paises)
class PaisesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Estados)
class EstadosAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Ciudades)
class CiudadesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Municipios)
class MunicipiosAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Parroquias)
class ParroquiasAdmin(admin.ModelAdmin):
    pass