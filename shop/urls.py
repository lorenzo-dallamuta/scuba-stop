from shop.models import Product
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, OrderViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
