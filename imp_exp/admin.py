from django.contrib import admin
from django.db.models import fields
from import_export import fields, resources, widgets
from import_export.widgets import ForeignKeyWidget
from import_export import resources
from rest_framework.authtoken import models

from inventory.models import Warehouse,Stock,Location
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



class StockResource(resources.ModelResource):

    # class ProductForeignKeyWidget(ForeignKeyWidget):
    #     def get_queryset(self, value, row):

    #         return self.model.objects.filter(
    #             product_id__exact=row["name"],
    #         )
    product_name = fields.Field(
        column_name='Product',
        attribute='product_id',
        widget=ForeignKeyWidget(Product,field='name')

     )
    # class LocationForeignKeyWiget(ForeignKeyWidget):
    #     def get_queryset(self, value, row):
    #         return self.model.objects.filter(
    #             location_id__exact=row["name"],
    #         )
    location_name = fields.Field(
        column_name='Location',
        attribute='location_id',
        widget=ForeignKeyWidget(Location,field='name')

     )

    
    class Meta:
        model =  Stock
        exclude = ('location_id','product_id','id' )
        





    




