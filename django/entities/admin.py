from django.contrib import admin
from entities import models


class AdministrativeUnitInline(admin.StackedInline):
    model = models.AdministrativeUnit
    min_num = 1


@admin.register(models.Entity)
class EntityAdmin(admin.ModelAdmin):
	inlines = (AdministrativeUnitInline,)
