from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    CartView,
    CartItemDeleteView,
    CategoryListView,
    SubCategoryListView,
    ProductListView,
)

urlpatterns = [
    path(
        "api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path(
        "subcategories/",
        SubCategoryListView.as_view(),
        name="subcategory_list",
    ),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("cart/", CartView.as_view(), name="cart"),
    path(
        "cart/item/<int:pk>/",
        CartItemDeleteView.as_view(),
        name="cart_item_delete",
    ),
]
