from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('order_item_id','order_reference','order_item_name','order_item_quantity','order_item_price','order_item_cost')