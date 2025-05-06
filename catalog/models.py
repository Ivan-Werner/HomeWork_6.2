from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование продукта')
    description = models.CharField(max_length=250, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/image', blank=True, null=True, verbose_name='Описание продукта')
    category = models.ForeignKey('Category',on_delete=models.SET_NULL, verbose_name='Описание', null=True, blank=True)
    price = models.FloatField(max_length=100, verbose_name='Цена за покупку')
    created_at = models.DateField(verbose_name='Дата создания')
    updated_at = models.DateField(verbose_name='Дата последнего изменения')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category']

    def __str__(self):
        return f'{self.name} {self.price}'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование категории')
    description = models.CharField(max_length=250, verbose_name='Описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
