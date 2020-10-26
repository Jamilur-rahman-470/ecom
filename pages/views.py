from pages.models import Contact
from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product
# Create your views here.
def index(request):
    featured = []
    top_product = []
    products = Product.objects.all()
    for i in products:
        if i.featured: 
            featured.append(i)
    for i in products:
        if i.top_product:
            top_product.append(i)

    context = {
        'featured': featured,
        'top_product': top_product,
    }
    return render(request, 'pages/index.html', context)


def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(
            name = name,
            email = email,
            message = message
        )
    return render(request, 'pages/contact.html', )