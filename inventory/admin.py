from django.contrib import admin

# Register your models here.

from inventory.models import Warehouse

admin.site.register(Warehouse)