from django import forms
from django.contrib import admin

from entities.models import AdministrativeUnit
from goods import models


@admin.register(models.Catalog)
class CatalogAdmin(admin.ModelAdmin):
    pass


class PurlieuInline(admin.StackedInline):
    model = models.Purlieu


class AssetsForm(forms.ModelForm):
    bulk_create = forms.IntegerField(label='N bienes extra', min_value=0, initial=0)

    class Meta:
        fields = ('catalog', 'name', 'code', 'administrative_unit', 'bulk_create')
        model = models.Assets


class AssetsInline(admin.StackedInline):
    model = models.Assets
    form = AssetsForm
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

        def set_correlative(assets):
            tam = 6
            span = '0'
            obj.assets.correlative = '{}-{}-{}-{}'.format(
                '{}'.format(assets.administrative_unit.entity.pk).rjust(tam, span),
                '{}'.format(assets.administrative_unit.pk).rjust(tam, span),
                '{}'.format(assets.catalog.pk).rjust(tam, span),
                '{}'.format(assets.pk).rjust(tam, span),
            )
            obj.assets.save()

        set_correlative(obj.assets)

        obj_model = obj.__class__.__name__.lower()
        assets = obj.assets

        for i in range(0, int(request.POST.get(
                            'assets-{}-bulk_create'.format(
                                request.POST.get('assets-__prefix__-bulk_create')
                            )
                        )
                    )
                ):

            assets.pk = None
            setattr(assets, obj_model, None)
            assets.save()

            obj.pk = None
            obj.save()
            setattr(assets, obj_model, obj)
            assets.save()

            set_correlative(assets)
        return super(GoodsAdmin, self).response_add(request, obj, post_url_continue)

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            formset = inline.get_formset(request, obj)
            if inline.__class__.__name__ == 'AssetsInline':
                if request.user.is_superuser is False:
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
