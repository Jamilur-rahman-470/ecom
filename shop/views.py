from shop.models import Product
from django.shortcuts import render

# Create your views here.

def single_product_page(request, slug):
    product = Product.objects.get(slug = slug)
    products = Product.objects.all()[:4]
    context = {
        'product': product,
        'products': products
    }
    return render(request, 'shop/product-single.html', context)