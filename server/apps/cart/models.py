import uuid

from django.db import models


# Create your models here.
from apps.menu.models import Menu


class Cart(models.Model):
    order_item_id = models.UUIDField(null=False, blank=False, primary_key=True, default=uuid.uuid4)
    order_item_name = models.CharField(null=False,max_length=155)
    order_item_quantity = models.IntegerField(null=False, default=0)
    order_item_price = models.IntegerField(null=False, default=0)
    order_item_cost = models.IntegerField(null=False, default=0)
    order_reference = models.UUIDField(null=False, blank=False)
    order_restaurant = models.UUIDField(null=False, blank=False,default=uuid.uuid4)

    def __str__(self):
        return self.order_item_name
