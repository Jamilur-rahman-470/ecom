from core.models import AddressAndInfo, Profile
from django.contrib import messages
from shop.models import Order, OrderItem, Product
from django.shortcuts import redirect, render
from core.decorators import allowed_user
from django.contrib.auth.decorators import login_required
import pdb
# Create your views here.


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
    total = 0
    for item in OrderItem.objects.filter(owner=request.user, is_ordered=False).all():
        if item.product.discounted_price > 0:
            total = total + item.product.discounted_price
        else:
            total = total + item.product.price
    context = {
        'items': OrderItem.objects.filter(owner=request.user, is_ordered=False).all(),
        'total': total
    }
    return render(request, 'shop/cart-page.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def add_to_cart(request, **kwargs):
    product = Product.objects.filter(id=kwargs.get('itemId', "")).get()
    OrderItem.objects.create(
        product=product, owner=request.user
    )


    return redirect('cart')


@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def delete_cart_item(request, **kwargs):
    OrderItem.objects.filter(id=kwargs.get('id', "")).delete()
    return redirect('cart')

# ORDER HELPER
def add_item_to_order(items, id):
    order = Order.objects.filter(ref_code = id).first()
    for item in items:
        order.items.add(item)

@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def checkout(request):
    order_items = OrderItem.objects.filter(
        owner=request.user).filter(is_ordered=False).all()

    address = AddressAndInfo.objects.filter(user=request.user).get()
    if(order_items.count() > 0):
        total = 0
        for item in OrderItem.objects.filter(owner=request.user).filter(is_ordered=False).all():
            if item.product.discounted_price > 0:
                total = total + item.product.discounted_price
            else:
                total = total + item.product.price
        order = Order.objects.create(
            owner = Profile.objects.get(user= request.user.id),
            shipping = address,
            price = total
        )
        new = Order.objects.get(items = None)
        print(new.ref_code)
        new.items.add(OrderItem.objects.get(owner=request.user, is_ordered=False))
        for item in order_items:
            item.is_ordered = True
            item.save()
        return redirect('dash')
    else:
        messages.success(request, 'No item in Cart')
        return redirect('index')
