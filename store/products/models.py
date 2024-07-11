from django.db import models
from django.conf import settings


class Category(models.Model):
    """Категория товара."""

    name = models.CharField(
        "Имя категории", unique=True, max_length=settings.LENGTH_OF_NAME_FIELDS
    )
    slug = models.SlugField(
        "Адрес категории",
        unique=True,
        db_index=False,
        max_length=settings.LENGTH_OF_NAME_FIELDS,
    )
    image_field = models.ImageField("Изображение категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    """Подкатегория товара."""

    name = models.CharField(
        "Имя подкатегории",
        unique=True,
        max_length=settings.LENGTH_OF_NAME_FIELDS,
    )
    slug = models.SlugField(
        "Адрес подкатегории",
        unique=True,
        db_index=False,
        max_length=settings.LENGTH_OF_NAME_FIELDS,
    )
    image_field = models.ImageField("Изображение подкатегории")
    parent_category = models.ForeignKey(
        Category,
        related_name="subcategories",
        on_delete=models.CASCADE,
        verbose_name="Родительская категория",
    )

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self):
        return self.name


class Product(models.Model):
    """Товар."""

    name = models.CharField(
        "Наименование", max_length=settings.LENGTH_OF_NAME_FIELDS, unique=True
    )
    slug = models.SlugField(
        "Адрес товара",
        unique=True,
        db_index=False,
        max_length=settings.LENGTH_OF_NAME_FIELDS,
    )
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE,
        verbose_name="Категория",
    )
    subcategory = models.ForeignKey(
        SubCategory,
        related_name="products",
        on_delete=models.CASCADE,
        verbose_name="Подкатегория",
    )
    price = models.IntegerField("Цена")
    image_small = models.ImageField("Маленькое изображение")
    image_medium = models.ImageField("Среднее изображение")
    image_large = models.ImageField("Большое изображение")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Cart(models.Model):
    """Корзина продуктов."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cart",
        verbose_name="Пользователь",
    )

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    def __str__(self):
        return f"Корзина {self.id}"


class CartItem(models.Model):
    """Продукт в корзине."""

    cart = models.ForeignKey(
        Cart,
        related_name="items",
        on_delete=models.CASCADE,
        verbose_name="Корзина",
    )
    product = models.ForeignKey(
        Product,
        related_name="cart_items",
        on_delete=models.CASCADE,
        verbose_name="Товар",
    )
    quantity = models.PositiveIntegerField("Количество", default=1)

    class Meta:
        verbose_name = "Продукт в корзине"
        verbose_name_plural = "Продукты в корзине"

    def __str__(self):
        return (
            f"{self.quantity} x {self.product.name} в корзине {self.cart.id}"
        )
