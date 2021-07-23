from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, OrderViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'products', ProductViewSet)
