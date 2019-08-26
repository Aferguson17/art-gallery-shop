from django.db import models
from gallery.models import Painting

class Cart(models.Model):
    new_cart_id = models.CharField(max_length=75, blank=True)
    date_added= models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.new_cart_id

class CartAddItem(models.Model):
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    class Meta:
        db_table = 'CartAddItem'

    def sub_total(self):
        return self.painting.price * self.quantity

    def __str__(self):
        return self.painting
