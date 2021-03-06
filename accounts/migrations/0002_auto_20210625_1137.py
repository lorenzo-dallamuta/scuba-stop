# Generated by Django 3.2 on 2021-06-25 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=85, verbose_name='Città'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='street_address',
            field=models.CharField(max_length=255, verbose_name='Indirizzo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zipcode',
            field=models.IntegerField(null=True, verbose_name='CAP'),
        ),
    ]
