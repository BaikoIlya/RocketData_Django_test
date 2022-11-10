import django_filters as filters

from sale_objects.models import SaleObject


class SaleObjectFilter(filters.FilterSet):
    country = filters.CharFilter(
        lookup_expr='istartswith',
        field_name='contacts__address__country'
    )
    id = filters.NumberFilter(field_name='products__id')

    class Meta:
        model = SaleObject
        fields = ['country', 'id']
