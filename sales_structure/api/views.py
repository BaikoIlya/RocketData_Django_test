from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response

from sale_objects.models import Product, SaleObject

from .filters import SaleObjectFilter
from .permission import WorkerOnly
from .serializers import (ProductSerializer, SaleObjectEditSerializer,
                          SaleObjectReadSerializer)


class SaleObjectViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с объектами торговой сети."""
    queryset = SaleObject.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = SaleObjectFilter

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return SaleObjectReadSerializer
        return SaleObjectEditSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return permissions.IsAuthenticated(),
        return WorkerOnly(),

    @action(
        detail=False,
        methods=['get', ],
        url_path='debt',
    )
    def debt(self, request):
        avg_debt = SaleObject.objects.aggregate(Avg('debt'))
        queryset = SaleObject.objects.all().filter(
            debt__gte=float(avg_debt['debt__avg'])
        )
        serializer = SaleObjectReadSerializer(
            queryset,
            many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductAPIView(generics.UpdateAPIView, generics.CreateAPIView,
                     generics.DestroyAPIView, viewsets.GenericViewSet):
    """Вью для добавления, обновления и удаления продуктов."""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
