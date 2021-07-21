from rest_framework import serializers
from shop.models import Category, Order, Product
from accounts.serializers import ProfileSerializer


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    sku = serializers.CharField(read_only=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
