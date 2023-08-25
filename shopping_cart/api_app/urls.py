from django.urls import path
from .views import ShoppingCart, ShoppingCartUpdate

urlpatterns = [
    path("cart-item/", ShoppingCart.as_view()),
    path("update-item/<int:item_id>", ShoppingCartUpdate.as_view()),
]