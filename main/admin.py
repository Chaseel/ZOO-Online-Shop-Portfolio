from django.contrib import admin
from main.models import ProductsCategory, Products, Basket

admin.site.register(Products)
admin.site.register(ProductsCategory)
 

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')