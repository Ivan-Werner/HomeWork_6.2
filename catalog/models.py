from django.db import models

from config import settings


class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name='Наименование продукта')
    description = models.CharField(max_length=250, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/image', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Описание категории', related_name='products')
    price = models.FloatField(max_length=100, verbose_name='Цена товара')
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateField(verbose_name='Дата последнего изменения', auto_now_add=True)
    in_active = models.BooleanField(default=True, verbose_name="В наличии")
    is_published = models.BooleanField(default=False, verbose_name="Статус публикации")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', related_name='products', null=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category']
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
            ('can_delete_product', 'Can delete product')
        ]

    def __str__(self):
        return f'{self.name} {self.price}'


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=100, verbose_name='Наименование категории', unique=True)
    description = models.CharField(max_length=250, verbose_name='Описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

