# Generated by Django 3.2.5 on 2021-07-21 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_options'),
        ('shop', '0004_rename_category_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
            preserve_default=False,
        ),
    ]
