from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin

from . import models


@admin.register(models.SaleObject)
class SaleObjectAdmin(MPTTModelAdmin):
    """Настройка Админ панели с фильтром и дополнительными ссылками."""
    list_display = ('name', 'show_parent',)
    list_display_links = ('name', 'show_parent', )
    list_filter = ('contacts__address__city',)
    actions = ['debt_to_zero', ]
    list_select_related = True

    def show_parent(self, obj):
        if obj.parent:
            app_label = obj._meta.app_label
            model_label = obj._meta.model_name
            url = reverse(
                f'admin:{app_label}_{model_label}_change',
                args=(obj.parent.id,)
            )
            return mark_safe(f'<a href="{url}">{obj.parent}</a>')
        return obj.parent

    show_parent.short_description = 'Поставщик'

    def debt_to_zero(self, request, queryset):
        queryset.update(debt=0)
    debt_to_zero.short_description = 'Обнуление задолженности'


admin.site.register(models.Address)
admin.site.register(models.Contact)
admin.site.register(models.Product)
