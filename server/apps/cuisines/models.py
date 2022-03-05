import uuid

from django.db import models

# Create your models here.
class Cuisines(models.Model):
    cuisine_id = models.UUIDField(null=False, blank=False, primary_key=True, default=uuid.uuid4, unique=True)
    cuisine_name = models.CharField(null=False, max_length=50,default="",unique=True)

    def __str__(self):
        return self.cuisine_name

    class Meta:
        ordering = ['cuisine_name']