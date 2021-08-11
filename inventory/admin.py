from django.contrib import admin

# Register your models here.

from inventory.models import Warehouse,Location,Stock

admin.site.register(Warehouse)
admin.site.register(Location)
admin.site.register(Stock)

