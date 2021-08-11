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

    def __str__(self):
        return self.location_id.name





