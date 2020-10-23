from django.urls import path
from . import views

urlpatterns = [
    path('product/<str:slug>', views.single_product_page, name='product.single')
]
