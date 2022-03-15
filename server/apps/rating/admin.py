from django.contrib import admin
from . import models

# Register your models here.
@admin.register((models.Rating))
class RatingAdmin(admin.ModelAdmin):
    list_display = ('rating_id','rating_rate','rating_restaurant')