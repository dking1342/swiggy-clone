import uuid

from django.db import models


# Create your models here.
class Discount(models.Model):
    discount_id = models.UUIDField(null=False, blank=False, primary_key=True, default=uuid.uuid4, unique=True)
    discount_code = models.CharField(null=False, max_length=10)
    discount_text = models.CharField(null=False, max_length=150)
    discount_amount = models.IntegerField(null=False, default=0)
    discount_created = models.DateTimeField(auto_now_add=True)
