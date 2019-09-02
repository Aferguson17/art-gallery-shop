from django.urls import path
from . import views

app_name='place_order'

urlpatterns = [
    path('confirmation/<int:order_id>/', views.confirmation, name='confirmation'),
]