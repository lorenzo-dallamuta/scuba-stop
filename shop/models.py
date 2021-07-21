from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from functools import reduce
from random import randint


class Category(models.Model):
    name = models.CharField(max_length=80)

    class Meta():
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    def makesku(self):
        nam = slugify(self.name)[:4]
        col = slugify(self.color)[:3]
        r = Product._meta.get_field('sku').max_length-len(nam)-len(col)-1
        l = [randint(1, 9) for i in range(r)]
        n = reduce(lambda a, b: str(a) + str(b), l)
        return f'{nam}-{col}-{self.demographic}-{n}'

    categories = models.ManyToManyField(Category, verbose_name=_('category'))
    name = models.CharField(max_length=30, unique=True, verbose_name=_('name'))
    brand = models.CharField(max_length=20, null=True,
                             blank=True, verbose_name=_('brand'))
    quantity = models.PositiveSmallIntegerField(
        verbose_name=_('quantity'), blank=True)
    color = models.CharField(max_length=20, null=True,
                             blank=True, verbose_name=_('color'))
    weight = models.DecimalField(
        max_digits=8, decimal_places=1, null=True, blank=True, verbose_name=_('weight'))
    demographic = models.CharField(
        choices=[('m', 'male'), ('f', 'woman'), ('c', 'child')], max_length=1, null=True, blank=True, verbose_name=_('demographic'))
    price_per_unit = models.DecimalField(
        max_digits=20, decimal_places=2, verbose_name=_('price per unit'))
    discount_per_unit = models.DecimalField(
        max_digits=2, decimal_places=2, default=0.0, blank=True, verbose_name=_('discount per unit'))
    sku = models.CharField(max_length=14, blank=True)
    slug = models.SlugField(max_length=80, unique=True, blank=True)

    class Meta():
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def save(self, *args, **kwargs):
        self.sku = self.makesku()
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# TODO: the admin for product should have list of related images and inline to create them
# class ProductImage(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     # TODO: save to subfolder with product id (possibly deal with it in save and post_save)
#     image = models.ImageField(upload_to='images/product/')


class Order(models.Model):
    discount = models.DecimalField(
        max_digits=2, decimal_places=2, default=0.0, blank=True)
    products = models.ManyToManyField(Product)

    class Meta():
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return str(self.id)
