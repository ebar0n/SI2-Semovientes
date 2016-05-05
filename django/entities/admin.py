from django.contrib import admin

from entities import models

@admin.register(models.Entity)
class EntityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AdministrativeUnit)
class AdministrativeUnitAdmin(admin.ModelAdmin):
    pass
