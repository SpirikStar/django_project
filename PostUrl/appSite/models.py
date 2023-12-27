from django.db import models

class FormUser(models.Model):
    name = models.CharField(
        verbose_name = "Имя",
        null=False,
        max_length=40,
        default="Неизвестно"
    )
    email = models.EmailField(
        verbose_name = "Почта",
        null=False,
        unique=True,
        db_index=True
    )
    age = models.IntegerField(
        verbose_name = "Возраст",
        null=False
    )
    def __str__(self):
        return self.email
    class Meta:
        verbose_name = "контактную информацию"
        verbose_name_plural = "Контактная информация"