from django.contrib import admin

from regions import models


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Estate)
class EstateAdmin(admin.ModelAdmin):
    pass


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Parish)
class ParishAdmin(admin.ModelAdmin):
    pass
