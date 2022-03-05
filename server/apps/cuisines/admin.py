from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Cuisines)
class CuisinesAdmin(admin.ModelAdmin):
    list_display = ('cuisine_id','cuisine_name')