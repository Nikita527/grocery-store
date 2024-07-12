from django.contrib import admin
from django.contrib.admin import register

from users.models import User


@register(User)
class MyUserAdmin(admin.ModelAdmin):
    """Админ панель для Пользователи."""

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
    )
    search_fields = (
        "username",
        "email",
    )
    ordering = ("username",)
    empty_value_display = "-пусто-"
    save_on_top = True
