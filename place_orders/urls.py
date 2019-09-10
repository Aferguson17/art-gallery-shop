from django.urls import path
from . import views

app_name='place_orders'

urlpatterns = [
    path('confirmation/<int:place_orders_id>/', views.confirmation, name='confirmation'),
]