from django.contrib import admin
from . import models


# Register your models here.
@admin.register((models.Userinfo))
class UserinfoAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name')
