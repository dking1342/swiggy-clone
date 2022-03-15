import uuid

from django.db import models
from apps.discount.models import Discount
from apps.restaurants.models import Restaurant


# Create your models here.
class Menu(models.Model):
    menu_id = models.UUIDField(null=False, blank=False, primary_key=True, default=uuid.uuid4)
    CATEGORY = (
        ('M', 'Main'),
        ('S', 'Side'),
        ('B', 'Beverage'),
        ('D', 'Dessert'),
        ('BR', 'Breakfast')
    )
    menu_category = models.CharField(max_length=2, choices=CATEGORY, null=False, default='M')
    menu_item = models.CharField(max_length=50, null=False, default="Hamburger")
    menu_description = models.CharField(max_length=250, blank=True)
    menu_price = models.IntegerField(default="199", null=False)
    menu_image = models.URLField(max_length=250)
    menu_hasOffer = models.BooleanField(default=False)
    menu_offer = models.ManyToManyField(Discount)
    menu_isBestseller = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default="")
    menu_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.menu_item

    class Meta:
        ordering = ['menu_category']
