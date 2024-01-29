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

class Product(models.Model):
    category1 = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=False,
        verbose_name = "Категория"
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
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = "Товары"