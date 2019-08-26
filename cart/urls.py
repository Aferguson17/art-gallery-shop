from django.urls import path
from . import views

app_name='cart'

urlpatterns = [
    path('add/<int:painting_id>/', views.cart_add, name='cart_add'),
    path('', views.item_in_cart, name='item_in_cart'),
]