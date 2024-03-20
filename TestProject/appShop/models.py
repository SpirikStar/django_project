from django.db import models

class ProductShop(models.Model):
    title = models.CharField('Имя товара', null=False, max_length=150)
    count = models.IntegerField(
        'Кол-во товаров на складе', 
        null=False, 
        default=0
    )
    price = models.FloatField(
        'Цена товара',
        null=False,
        default=0.0
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "Товары"
