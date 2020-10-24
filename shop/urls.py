from shop.views import add_to_cart
from django.urls import path
from . import views

urlpatterns = [
    path('product/<str:slug>', views.single_product_page, name='product.single'),
    path('user/cart', views.cart_page, name='cart'),
    path('user/to-cart/<int:itemId>', views.add_to_cart, name='to-cart'),
    path('user/remove/<int:id>', views.delete_cart_item, name='remove-cart-item'),
    path('user/checkout', views.checkout, name='checkout')
]
