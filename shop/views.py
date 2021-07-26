from rest_framework import viewsets
from shop.models import Category, Product
from shop.permissions import IsAdminOrReadOnly, IsOwnerOrAdmin
from shop.serializers import CategorySerializer, OrderSerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = (IsOwnerOrAdmin,)

    def get_queryset(self):
        return self.request.user.profile.orders.all()

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
