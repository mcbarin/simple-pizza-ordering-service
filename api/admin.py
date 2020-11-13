from django.contrib import admin
from api import models


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Order, OrderAdmin)
