from django.contrib import admin
from sale.models import SaleOrder,SaleOrderLine,Coupon
# Register your models here.

admin.site.register(SaleOrder)
admin.site.register(SaleOrderLine)
admin.site.register(Coupon)