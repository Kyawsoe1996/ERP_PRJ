from django.contrib import admin
from customer.models  import Customer
# Register your models here.

from .models import ProductUOM,ProductCategory,Product


admin.site.register(ProductCategory)
admin.site.register(ProductUOM)

#I have Customer model,, what i want is only vendor show in foreignkey
#  i have field in Customer table is_vendor, or , is_customer
#i only need vendor list  in this Product Model
#https://docs.djangoproject.com/en/3.2/ref/contrib/admin/
#29-08-2021 7:40pm at home
class CustomProductAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "vendor":
          kwargs["queryset"] = Customer.objects.filter(is_vendor=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Product,CustomProductAdmin)
# admin.site.register(Product)
