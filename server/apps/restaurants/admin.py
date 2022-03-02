from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('restaurant_id', 'restaurant_name')


