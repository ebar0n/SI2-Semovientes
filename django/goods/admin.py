from django.contrib import admin
from goods import models
from entities.models import AdministrativeUnit

@admin.register(models.Catalog)
class CatalogAdmin(admin.ModelAdmin):
    pass


class PurlieuInline(admin.StackedInline):
    model = models.Purlieu

class AssetsInline(admin.StackedInline):
    model = models.Assets
    fields = ('catalog', 'name', 'code', 'administrative_unit')
    min_num = 1


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_name', 'get_email_correlative')
    list_filter = ()
    search_fields = ()
    inlines = (AssetsInline,)
    
    def get_name(self, obj):
        return obj.assets.name
    get_name.short_description = 'Nombre'

    def get_email_correlative(self, obj):
        return obj.assets.correlative
    get_email_correlative.short_description = 'Correlativo'

    def response_add(self, request, obj, post_url_continue=None):
        tam = 6
        span = '0'
        obj.assets.correlative = '{}-{}-{}-{}'.format(
            '{}'.format(obj.assets.administrative_unit.entity.pk).rjust(tam, span),
            '{}'.format(obj.assets.administrative_unit.pk).rjust(tam, span),
            '{}'.format(obj.assets.pk).rjust(tam, span),
            '{}'.format(obj.pk).rjust(tam, span),
        )
        obj.assets.save()
        return super(GoodsAdmin, self).response_add(request, obj, post_url_continue)

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            formset = inline.get_formset(request, obj)
            if request.user.is_superuser is False:
                if inline.__class__.__name__ == 'AssetsInline':
                    formset.form.base_fields['administrative_unit'].queryset = AdministrativeUnit.objects.filter(
                        entity=request.user.entity)
            yield formset, inline


@admin.register(models.Furnishing)
class FurnishingAdmin(GoodsAdmin):
    pass


@admin.register(models.Property)
class PropertyAdmin(GoodsAdmin):
    inlines = (PurlieuInline, AssetsInline,)


@admin.register(models.Semoviente)
class SemovienteAdmin(GoodsAdmin):
    pass