import uuid

from django.db import models


# Create your models here.
class Userinfo(models.Model):
    user_id = models.UUIDField(null=False, blank=False, primary_key=True, default=uuid.uuid4, unique=True)
    user_name = models.CharField(null=False, default="Username", max_length=50)
    user_phone = models.CharField(null=False, default="", max_length=12)
    user_email = models.CharField(null=False, default="", max_length=255)

    def __str__(self):
        return self.user_phone
