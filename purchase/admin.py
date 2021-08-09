from django.contrib import admin

# Register your models here.
from .models import PurchaseOrder,PurchaseOrderLine


admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderLine)