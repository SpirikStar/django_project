# Generated by Django 5.0 on 2024-03-18 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenerateDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(default=datetime.datetime.now, editable=False, verbose_name='Дата и время')),
                ('status', models.BooleanField(default=False, help_text='Да (Активный) / Нет (Не активный)', verbose_name='Разрешение')),
            ],
            options={
                'verbose_name': 'дату и время',
                'verbose_name_plural': 'Дата и время',
            },
        ),
        migrations.CreateModel(
            name='GenerateNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=346, verbose_name='Число')),
                ('status', models.BooleanField(default=True, help_text='Да (Активный) / Нет (Не активный)', verbose_name='Разрешение')),
            ],
            options={
                'verbose_name': 'число',
                'verbose_name_plural': 'Числа',
            },
        ),
    ]
