from django.shortcuts import render
from .models import placeOrder

def confirmation(request, place_order_id):
    if order_id:
        customer_order =  get_object_or_404(placeOrder, id=place_orders_id)
    return render(request, 'confirmation.html', {'customer_order':customer_order})
