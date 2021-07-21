from rest_framework import viewsets
from shop.models import Category, Order, Product
from shop.serializers import CategorySerializer, OrderSerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return self.request.user.profile.orders.all()

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
