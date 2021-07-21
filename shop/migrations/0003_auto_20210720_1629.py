# Generated by Django 3.2 on 2021-07-20 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210625_1137'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='quantity'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='shop.Category', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='demographic',
            field=models.CharField(blank=True, choices=[('m', 'male'), ('f', 'woman'), ('c', 'child')], max_length=1, null=True, verbose_name='demographic'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_per_unit',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=2, verbose_name='discount per unit'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_per_unit',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='price per unit'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=8, null=True, verbose_name='weight'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
