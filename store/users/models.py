from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Пользователь магазина."""

    email = models.EmailField(
        "Адрес электроной почты",
        max_length=settings.LENGTH_OF_FIELDS_SHORT,
        unique=True,
    )
    username = models.CharField(
        "Никнейм",
        max_length=settings.LENGTH_OF_NAME_FIELDS,
        unique=True,
    )
    first_name = models.CharField(
        "Имя",
        max_length=settings.LENGTH_OF_FIELDS_SHORT,
    )
    last_name = models.CharField(
        "Фамилия",
        max_length=settings.LENGTH_OF_FIELDS_SHORT,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("username",)

    def __str__(self) -> str:
        return f"{self.username}: {self.email}"
