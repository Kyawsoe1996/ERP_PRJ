from django.contrib import admin
from django.db.models import fields

from import_export import resources

from inventory.models import Warehouse
from product.models import Product
# Register your models here.



class WarehouseResource(resources.ModelResource):

    class Meta:
        model = Warehouse
        fields = ('name','vendor__name')



#For Product Name showing export 

class ProductNameResource(resources.ModelResource):

    class Meta:
        model = Product
        fields = ('name')




    




