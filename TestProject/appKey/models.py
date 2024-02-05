from django.db import models

class Category(models.Model):
    title = models.TextField(
        'Категория',
        null=False,
        help_text = 'Например: квартира'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'

class Subcategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=False,
        verbose_name = "Категория"
    ) 
    title = models.CharField(
        'Название подкатегории',
        max_length = 100,
        null=False
    )
    def __str__(self):
        return f'Категория: {self.category.title} | Подкатегория: {self.title}'
    class Meta:
        verbose_name = 'подкатегорию'
        verbose_name_plural = 'Подкатегории'

class Product(models.Model):
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name = "Подкатегория"
    )
    title = models.TextField(
        'Заголовок',
        null=False,
        help_text = 'Например: Продаю земельный участок'
    )
    desc = models.TextField(
        'Описание',
        null=True,
        blank=True
    )    
    price = models.FloatField(
        'Стоимость',
        null=False
    )
    currency = models.CharField(
        'Валюта', 
        null=False,
        choices = [
            ('RU', 'Рубль'),
            ('US', 'Доллар'),
            ('CHINA', 'Юань'),
            ('EU', 'Евро')
        ],
        max_length = 10,
        default = 'RU'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = "Товары"

class PhotosProduct(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete = models.CASCADE,
        null=True,
        blank=True,
        verbose_name = "Продукт"
    )
    photo = models.ImageField(
        verbose_name = "Изображение",
        null=False,
        upload_to='product'
    )
    def __str__(self):
        return str(self.photo)
    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = "Изображения продуктов"