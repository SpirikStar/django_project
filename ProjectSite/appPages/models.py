from django.db import models
import datetime


class News(models.Model):
    title = models.CharField(
        'Заголовок',
        null=False,
        max_length=200,
    )
    content = models.TextField(
        'Содержание',
        null=True,
        blank=True
    )
    date = models.DateField(
        'Дата',
        default=datetime.datetime.today,
        null=False
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'Новости'
