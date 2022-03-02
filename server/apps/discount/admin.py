from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('discount_id', 'discount_code', 'discount_text')
