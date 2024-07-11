from django.contrib import admin
from django.contrib.admin import register

from products.models import Cart, CartItem, Product, Category, SubCategory

EMTY_MSG = "-пусто-"


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админ панель для Продуктов."""

    list_display = (
        "name",
        "category",
        "subcategory",
        "slug",
    )
    search_fields = ("name",)
    list_filter = (
        "category",
        "subcategory",
    )
    prepopulated_fields = {"slug": ("name",)}
    empty_value_display = EMTY_MSG


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Админ панель для Категорий."""

    list_display = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    empty_value_display = EMTY_MSG


@register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    """Админ панель для Категорий."""

    list_display = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    empty_value_display = EMTY_MSG


@register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user",)
    empty_value_display = EMTY_MSG


@register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "product", "quantity")
    empty_value_display = EMTY_MSG
