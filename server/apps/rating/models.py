import uuid

from django.db import models


# Create your models here.
class Rating(models.Model):
    rating_id = models.UUIDField(null=False, blank=False, primary_key=True, default=uuid.uuid4)
    rating_rate = models.IntegerField(null=False, default=1)
    rating_order_reference = models.UUIDField(null=False, blank=False)
    rating_restaurant = models.UUIDField(null=False, blank=False)

    def __str__(self):
        return "rating"
