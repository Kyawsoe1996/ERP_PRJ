from django.contrib import admin

# Register your models here.

from .models import ProductUOM,ProductCategory,Product

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductUOM)
