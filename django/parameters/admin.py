from django.contrib import admin

from parameters import models


# Register your models here.
@admin.register(models.Function)
class FunctionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Gender)
class GenderAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Breed)
class BreedAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MeasureUnit)
class MeasureUnitAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Colour)
class ColourAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Make)
class MakeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Model)
class ModelAdmin(admin.ModelAdmin):
    pass
