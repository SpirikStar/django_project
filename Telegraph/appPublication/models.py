from tinymce.models import HTMLField
from django.db import models
import datetime
import uuid

class PubNews(models.Model):
    content = HTMLField(
        verbose_name="Содержание",
        null=False
    )
    date_time = models.DateTimeField(
        verbose_name="Дата и время публикации",
        null=False,
        default=datetime.datetime.now
    )
    name_url = models.CharField(
        verbose_name="Имя ссылки",
        max_length=10,
        null=False,
    )
    count = models.IntegerField(
        verbose_name="Просмотры",
        default = 0,
        null=False
    )
    def __str__(self):
        return self.name_url
    class Meta:
        verbose_name = "публикацию"
        verbose_name_plural = "Публикации"