from django.contrib import admin
from .models import placeOrder, yourItem

class yourItemAdmin(admin.TabularInline):
    model = yourItem
    fieldsets = [('Painting', {'fields':['painting'],}),('Price', {'fields':['price'],}),('Quantity', {'fields':['quantity'],}),]
    readonly_fields = ['painting','price','quantity']
    can_delete= False

@admin.register(placeOrder)
class placeOrderAdmin(admin.ModelAdmin):
    list_display = ['billingName','emailAddress', 'dateCreated']
    list_display_links = ['billingName']
    search_fields = ['billingName','emailAddress']
    readonly_fields = ['token','total','billingName','emailAddress',
                    'billingAddress','billingCity','billingPostal','dateCreated']
    fieldsets = [
        ('ORDER INFORMATION',{'fields': ['created','id','token','total']}),
        ('CUSTOMER INFORMATION', {'fields': ['billingName','emailAddress','billingAddress','billingCity','billingPostal']}),
    ]

    inlines = [
        yourItemAdmin, 
    ]

    def add_permission_yes(self, request, obj=None):
        return False

    def delete_permission_yes(self, request, obj=None): 
        return False