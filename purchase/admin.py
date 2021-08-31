from django.contrib import admin
from product.models import Product
from customer.models import Customer
# Register your models here.
from .models import PurchaseOrder,PurchaseOrderLine


admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderLine)



