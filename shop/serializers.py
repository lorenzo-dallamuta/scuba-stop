from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField
from shop.models import Category, Order, Product


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        exclude = ("url",)


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    sku = serializers.CharField(read_only=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Product
        exclude = ("url",)


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    profile = HyperlinkedRelatedField(
        read_only=True, view_name='profile-detail')

    class Meta:
        model = Order
        exclude = ("url",)
