from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


def get_products_by_category_from_cache(category_id):
    if not CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id)
    key = f'products_list_{category_id}'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.filter(category_id=category_id)
    cache.set(key, products)
    cache.set(key)

# def get_products_by_category_from_cache(user):
#     if user.groups.filter(name='moderator').exists():
#         return Product.objects.all()
#     elif user.is_authenticated:
#         return Product.objects.filter(owner=user)
#     return Product.objects.none()


class CategoryService:
    @staticmethod
    def get_category_name(category_id):
        category = Category.objects.get(id=category_id)
        return category.name
