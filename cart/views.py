import stripe
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_list_or_404
from gallery.models import Painting
from .models import Cart, CartAddItem


# session id created view #
def new_cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

# items added to new cart view#
def cart_add(request, painting_id):
    painting = Painting.objects.get(id=painting_id)
    try:
        cart = Cart.objects.get(new_cart_id=new_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(new_cart_id =new_cart_id(request))
        cart.save()
    try:
        add_cart_item = CartAddItem.objects.get(painting=painting, cart=cart)
        if add_cart_item.quantity < add_cart_item.painting.quantity:
            add_cart_item.quantity += 1
            add_cart_item.save()
    except CartAddItem.DoesNotExist:
        add_cart_item = CartAddItem.objects.create(painting = painting, quantity = 1, cart = cart)
        add_cart_item.save()
    return redirect('cart:item_in_cart')

# funct that checks new items in cart view #
def item_in_cart(request, total=0, counter=0, add_cart_items = None):
    try:
        cart = Cart.objects.get(new_cart_id=new_cart_id(request))
        add_cart_items = CartAddItem.objects.filter(cart=cart, active=True)
        for add_cart_item in add_cart_items:
            total += (add_cart_item.painting.price * add_cart_item.quantity)
            counter += add_cart_item.quantity
    except ObjectDoesNotExist: pass

#stripe data
    stripe.api_key = settings.STRIPE_SECRET_KEY
    data_key = settings.STRIPE_PUBLISHABLE_KEY
    description = 'Ferguson Virtual Gallery'
    stripe_cc_total = int(total * 100)
    if request.method == 'POST':
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            billingName = request.POST['stripeBillingName']
            customer = stripe.Customer.create(
                email = email,
            )
            charge = stripe.Charge.create(
                amount=stripe_cc_total,
                currency="usd",
                customer=customer.id,
                description=description,
            )
            try:
                items_in_cart = placeOrder.objects.create(
                        token = token, 
                        email = email, 
                        total= total,
                        billingName = billingName, 
                    )
                items_in_cart.save()
                for order_item_added in add_cart_items:
                    yi = Order.objects.create(
                        painting = order_item_added.painting.title,
                        price = order_item_added.painting.price,
                        quantity = order_item_added.quantity,
                        order = items_in_cart
                    )
                    yi.save()

#first part remove qty added from the quantity still available#
                    paintings = Painting.objects.get(id=order_item_added.painting.id)
                    paintings.quantity = int(order_item_added.painting.quantity - order_item_added.quantity)
                    paintings.save()
# deletes the items from the cart after it has been saved. 
                    order_item_added.delete()
                return redirect('gallery:shopByStyle')
            except stripe.error.CardError as e: 
                return False, e
        except ObjectDoesNotExist: pass
    return render(request, 'cart.html', dict(add_cart_items = add_cart_items, total = total, stripe_cc_total = stripe_cc_total, counter = counter, 
     data_key = data_key, description = description
    ))