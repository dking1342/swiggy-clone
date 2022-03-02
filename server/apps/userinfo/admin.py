from django.contrib import admin
from . import models


# Register your models here.
@admin.register((models.Userinfo))
class UserinfoAdmin(admin.ModelAdmin):
    list_display = ('userinfo_id', 'userinfo_username')
