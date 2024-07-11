from rest_framework import serializers
from .models import Cart, CartItem, Product, Category, SubCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug", "image_field"]


class SubCategorySerializer(serializers.ModelSerializer):
    parent_category = CategorySerializer()

    class Meta:
        model = SubCategory
        fields = ["name", "slug", "image_field", "parent_category"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "slug",
            "category",
            "subcategory",
            "price",
            "image_small",
            "image_medium",
            "image_large",
        ]


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ["product", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ["id", "items"]
