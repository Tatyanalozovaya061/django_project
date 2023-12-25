from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование продукта')
    product_description = models.TextField(max_length=150, verbose_name='Описание продукта')
    product_image = models.ImageField(upload_to='images/', verbose_name='Изображение продукта', **NULLABLE)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория продукта')
    product_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость продукта за единицу')
    product_date_created = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Дата создания записи')  # Automatically set the date of
    product_date_last_modified = models.DateTimeField(auto_now=True,
                                              verbose_name='Дата последнего изменения записи')  # Automatically set\

    in_stock = models.BooleanField(default=True, verbose_name='В наличии имеется')

    def __str__(self):
        return f'{self.product_name} {self.product_description}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование категории')
    category_description = models.TextField(max_length=150, verbose_name='Описание категории')
    # created_at = models.DateTimeField(auto_now_add=True,
    #                                     verbose_name='Дата создания')

    def __str__(self):
        return f'{self.category_name} - {self.category_description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
