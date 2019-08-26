from .models import Cart, CartAddItem
from .views import new_cart_id

def counter(request):
    number_of_painting = 0
    if 'admin' in request.path: 
        return {}
    else:
        try:
            cart = Cart.objects.filter(new_cart_id=new_cart_id(request))
            add_cart_items = CartAddItem.objects.all().filter(cart=cart[:1])
            for add_cart_item in add_cart_items: number_of_painting += add_cart_item.quantity
        except Cart.DoesNotExist: number_of_painting  = 0 
    return dict(number_of_painting = number_of_painting) 