from django.db import models
from appPublication.models import PubNews
import datetime

class StaticLink(models.Model):
    pub_news = models.ForeignKey(
        PubNews,
        on_delete=models.CASCADE,
        null=False,
        verbose_name="Публикация"
    )
    os = models.CharField(
        verbose_name="Операцационная система",
        null=True,
        blank=True,
        max_length=150
    )
    browser = models.CharField(
        verbose_name="Браузер",
        null=True,
        blank=True,
        max_length=150
    )
    is_bot = models.BooleanField(
        verbose_name="Бот",
        choices=[
            (True, "Да"),
            (False, "Нет"),
        ],
        default=False,
        null=True,
        blank=True,
    )
    is_touch_capable = models.BooleanField(
        verbose_name="Поддержка сенсорного экрана",
        choices=[
            (True, "Да"),
            (False, "Нет"),
            (False, "Нет"),
        ],
        default=False,
        null=True,
        blank=True,
    )
    type_device = models.CharField(
        verbose_name="Тип устройства",
        choices=[
            ('mobile', "Телефон"),
            ('tablet', "Планшет"),
            ('pc', "ПК"),
        ],
        default=False,
        null=True,
        blank=True,
        max_length=150
    )
    date_time = models.DateTimeField(
        verbose_name="Дата и время",
        default=datetime.datetime.now,
        null=False
    )
    def __str__(self):
        return self.pub_news.name_url
    class Meta:
        verbose_name="историю"
        verbose_name_plural="Просмотры"