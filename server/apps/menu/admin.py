from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('menu_id', 'menu_item', 'menu_price')
