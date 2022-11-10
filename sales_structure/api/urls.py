from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import ProductAPIView, SaleObjectViewSet

router = SimpleRouter()
router.register('product', ProductAPIView, basename='products')
router.register('sale_objects', SaleObjectViewSet, basename='objects')
urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
