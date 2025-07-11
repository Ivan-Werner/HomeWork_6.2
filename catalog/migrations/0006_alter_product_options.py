# Generated by Django 4.2.2 on 2025-06-06 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_product_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', 'category'], 'permissions': [('can_unpublish_product', 'Can unpublish product'), ('can_delete_product', 'Can delete product')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
