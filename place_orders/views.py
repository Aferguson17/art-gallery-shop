from django.shortcuts import render, get_object_or_404
from .models import placeOrder, yourItem

def confirmation(request, place_orders_id):
    if place_orders_id:
        customer_order =  get_object_or_404(placeOrder, id=place_orders_id)
    return render(request, 'confirmation.html', {'customer_order': customer_order})
