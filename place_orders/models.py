from django.db import models

class placeOrder(models.Model):
    token = models.CharField(max_length=75, blank=True)
    dateCreated = models.DateField(auto_now=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Total')
    emailAddress = models.EmailField(max_length=75, blank=True, verbose_name='Email Address')
    billingName = models.CharField(max_length=75, blank=True)
    billingAddress = models.CharField(max_length=75, blank=True)
    billingCity = models.CharField(max_length=75, blank=True)
    billingPostal = models.CharField(max_length=75, blank=True)

    class Meta:
        db_table = 'placeOrder'
        ordering = ['-dateCreated']
    
    def __str__(self):
        return str(self.id)

class yourItem(models.Model):
    painting = models.CharField(max_length=75)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Price')
    quantity = models.IntegerField()
    place_orders = models.ForeignKey(placeOrder, on_delete=models.CASCADE)

    class Meta:
        db_table = 'yourItem'
    
    def sub_total(self):
        return self.price * self.quantity
    
    def __str__(self):
        return self.painting
