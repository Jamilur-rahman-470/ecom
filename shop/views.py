from django.contrib import messages
from django.contrib.messages.api import success
from django.http import request
from shop.models import Order, OrderItem, Product, WishList
from django.shortcuts import redirect, render
from core.decorators import allowed_user
from django.contrib.auth.decorators import login_required
# Create your views here.
def shop_page(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'shop/shop-page.html', context)
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


@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def add_to_wish_list(request, **kwargs):
    list  = WishList.objects.filter(owner = request.user, item = Product.objects.get(id = kwargs.get('id'))).all()

    if list.exists():
        messages.success(request, 'Already in wishlist')
        return redirect('wishlist')
    else:

        wishlist = WishList(
                owner = request.user,
                item = Product.objects.get(id = kwargs.get('id'))
            )
        wishlist.save()
            
        context = {
            'wishlist': WishList.objects.filter(owner = request.user).all()
        }

        return render(request, 'shop/wish-page.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def delete_wish(request, **kwargs):
    WishList.objects.filter(id = kwargs.get('id')).delete()
    return redirect('wishlist')

@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def clear_wish(request):
    wishlist = WishList.objects.filter(owner = request.user).all()
    for item in wishlist:
        item.delete()
    return redirect('wishlist')


@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def wishlist_page(request):
    context = {
        'wishlist': WishList.objects.filter(owner = request.user).all()
    }
    return render(request, 'shop/wish-page.html', context)



@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def create_cart_from_wishlist(request):
    wishlist = WishList.objects.filter(owner = request.user).all()
    for item in wishlist:
        p = 0
        if item.item.discounted_price > 0:
            p = item.item.discounted_price
        else:
            p = item.item.price
        OrderItem.objects.create(
            owner = request.user,
            price = p,
            item = item.item
        )
    
    return redirect('cart')