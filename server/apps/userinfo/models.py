import uuid

from django.db import models


# Create your models here.
class Userinfo(models.Model):
    userinfo_id = models.UUIDField(null=False, blank=False, primary_key=True, default=uuid.uuid4, unique=True)
    userinfo_username = models.CharField(null=False, default="Username", max_length=50)
    userinfo_address_1 = models.CharField(max_length=128)
    userinfo_address_2 = models.CharField(max_length=128, blank=True)
    userinfo_city = models.CharField(max_length=64, default="New York City")
    userinfo_zip_code = models.CharField(max_length=5, default="90210")

    def __str__(self):
        return self.userinfo_username
