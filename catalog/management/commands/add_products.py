from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add products to the database'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        category,_ = Category.objects.get_or_create(name='ПК', description='Персональный компьютер')
        products = [
            {'name': 'BLOODY', 'description': 'Мощный игровой ПК', 'category': category, 'price': 60000},
            {'name': 'Acer', 'description': 'Компьютер', 'category': category, 'price': 50000}
        ]

        category,_ = Category.objects.get_or_create(name='Ноутбук', description='Мощный Laptop')
        products_2 = [
            {'name': 'Dell', 'description': 'Легкий и мощный ноутбук', 'category': category, 'price': 50000},
            {'name': 'Asus', 'description': 'Ультрабук', 'category': category, 'price': 40000}
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product}'))

        for product_data in products_2:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product}'))
