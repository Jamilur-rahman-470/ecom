from shop.views import add_to_cart, add_to_wish_list, shop_page
from django.urls import path
from . import views

urlpatterns = [
    path('product/<str:slug>', views.single_product_page, name='product.single'),
    path('user/cart', views.cart_page, name='cart'),
    path('user/to-cart/<int:itemId>', views.add_to_cart, name='to-cart'),
    path('user/remove/<int:id>', views.delete_cart_item, name='remove-cart-item'),
    path('user/checkout', views.checkout, name='checkout'),
    path('user/wishlist/', views.wishlist_page, name='wishlist'),
    path('user/wishlist/<int:id>', views.add_to_wish_list, name='wishlist.add'),
    path('user/wishlist-delete/<int:id>', views.delete_wish, name='wishlist.delete'),
    path('user/wishlist/clear', views.clear_wish, name='wishlist.delete.all'),
    path('user/wish-list-to-cart', views.create_cart_from_wishlist, name='wishlist.cart'),
    path('shop/', views.shop_page, name='shop')
]


