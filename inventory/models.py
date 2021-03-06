from django.db import models
from django.urls import reverse
from product.models import Product
from customer.models import Customer

# Create your models here.


class Warehouse(models.Model):
    

    name = models.CharField(max_length=50)
    vendor =  models.ForeignKey(Customer,related_name="warehouses",on_delete=models.CASCADE,null=True)


    class Meta:
     

        verbose_name = 'Warehouse'
        # verbose_name_plural = 'Warehouses'

    def __str__(self):
        return self.name

    
    def get_absolute_url(self):
        return reverse('warehouse-detail', kwargs={'pk': self.pk})

class Location(models.Model):
    name = models.CharField(max_length=20)
    warehouse_id = models.ForeignKey(Warehouse,related_name="locations",on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    # product_upload = models.FieldFile(blank=True,null=True)
    product_name_csv_file = models.FileField(upload_to='product-name-lists',blank=True, null=True)


    class Meta:

        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
    
    
    def __str__(self):
        return self.name



class Stock(models.Model):

    location_id = models.ForeignKey(Location,related_name="stocks",on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,related_name="stocks",on_delete=models.CASCADE,blank=True,null=True)
    quantity = models.IntegerField()
    class Meta:

        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'
        unique_together = ('location_id', 'product_id')

  
        

    def __str__(self):
        warehouse = self.location_id.warehouse_id.name
        p_name =self.product_id.name
        qty = self.quantity
        location = self.location_id.name
        name = f" {warehouse}-{location}-{qty}-{p_name}"
        return name

class StockUpload(models.Model):
  date_uploaded       = models.DateTimeField(auto_now=True)
  csv_file            = models.FileField(upload_to='stock_upload')

  




