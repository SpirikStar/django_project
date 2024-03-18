from django.db import models
import random, datetime

def generate_number():
    return random.randint(100, 600)

class GenerateNumber(models.Model):
    number = models.IntegerField('Число', null=False, default=generate_number)
    status = models.BooleanField(
        'Разрешение', 
        null=False, 
        default=True,
        help_text ="Да (Активный) / Нет (Не активный)"
    )
    def __int__(self):
        return self.number
    class Meta:
        verbose_name = "число"
        verbose_name_plural = "Числа"

class GenerateDate(models.Model):
    date_time = models.DateTimeField(
        'Дата и время',
        null=False,
        default=datetime.datetime.now,
        editable=False
    )
    status = models.BooleanField(
        'Разрешение', 
        null=True,
        blank=True,
        default=True,
        help_text ="Да (Активный) / Нет (Не активный)"
    )
    def __str__(self):
        return str(self.date_time)
    class Meta:
        verbose_name = "дату и время"
        verbose_name_plural = "Дата и время"