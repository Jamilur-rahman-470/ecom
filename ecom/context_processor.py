from shop.models import OrderItem, WishList

def get_cart_and_wish_count(request):
    
    if request.user.is_authenticated:

        cart = OrderItem.objects.filter(owner = request.user, is_ordered = False).count()
        wish = WishList.objects.filter(owner = request.user).count()
        return {
            'cart_count': cart,
            'wish_count': wish
        }

    else: 
        return {
            'cart_count': 0,
            'wish_count': 0
        }