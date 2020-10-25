from shop.models import Order, OrderItem, Product
from django.shortcuts import redirect, render
from core.decorators import allowed_user
from django.contrib.auth.decorators import login_required
# Create your views here.

def get_total(items):
    total = 0
    for i in items:
        if i.item.discounted_price > 0:
            total = total + i.item.discounted_price
        else:
            total = total + i.item.price
    return total



def single_product_page(request, slug):
    product = Product.objects.get(slug=slug)
    products = Product.objects.all()[:4]
    context = {
        'product': product,
        'products': products
    }
    return render(request, 'shop/product-single.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def cart_page(request):
    items = OrderItem.objects.filter(is_ordered = False, owner = request.user).all()

    context ={
        "cart": items,
        'total': get_total(items)
    }
    return render(request, 'shop/cart-page.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def add_to_cart(request, **kwargs):
    product = Product.objects.get(id = kwargs.get('itemId'))
    p = 0
    if product.discounted_price > 0:
        p = product.discounted_price
    else:
        p = product.price
    OrderItem.objects.create(
        owner = request.user,
        item = product,
        price = p
    )
    return redirect('cart')



@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def delete_cart_item(request, **kwargs):
    OrderItem.objects.filter(id = kwargs.get('id')).delete()
    return redirect('cart')



@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def checkout(request):
    items = OrderItem.objects.filter(owner = request.user, is_ordered = False).all()
    order = Order(
        owner = request.user,
        price = get_total(items)
    )
    order.save()
    for i in items:
        order.items.add(OrderItem.objects.get(id = i.id))
        order.save()
    for i in items:
        i.is_ordered = True
        i.save()
    
    return redirect('dash')
