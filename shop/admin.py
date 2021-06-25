from shop.models import Category, Order, Product
from django.contrib import admin
from django.contrib.admin import ModelAdmin


class ProductAdmin(ModelAdmin):
    list_display = ('name', 'sku')

    def add_view(self, *args, **kwargs):
        self.exclude = ('sku', 'slug')
        return super().add_view(*args, **kwargs)


admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Product, ProductAdmin)
