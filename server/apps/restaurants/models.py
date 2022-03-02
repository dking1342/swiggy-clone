import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models
from apps.discount.models import Discount


# Create your models here.
class Restaurant(models.Model):
    restaurant_id = models.UUIDField(null=False, blank=False, primary_key=True, default=uuid.uuid4, unique=True)
    restaurant_name = models.CharField(null=False, max_length=50, default="Food Stuff")
    restaurant_address_1 = models.CharField(max_length=128, default="123 Main St", null=False)
    restaurant_address_2 = models.CharField(max_length=128, blank=True)
    restaurant_city = models.CharField(max_length=64, default="New York City", null=False)
    restaurant_zip_code = models.CharField(max_length=5, default="90210", null=False)
    STATE_SELECTION = (
        ('AL', 'Alabama'),
        ('CA', 'California'),
        ('MI', 'Michigan'),
        ('WI', 'Wisconsin')
    )
    restaurant_state = models.CharField(max_length=2, choices=STATE_SELECTION, null=False, default="AL")
    restaurant_cuisines = ArrayField(models.CharField(max_length=20, blank=True), size=20)
    restaurant_main_img = models.URLField(max_length=200, default="")
    discount_isValid = models.BooleanField(default=False)
    discounts = models.ManyToManyField(Discount)
    restaurant_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.restaurant_name

    class Meta:
        ordering = ['restaurant_name']
