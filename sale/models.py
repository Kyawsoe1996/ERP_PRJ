from django.db import models
from django.db.models.fields import related
from customer.models import Customer
from product.models import Product
import  datetime

# Create your models here.




STATUS = (
    ('q', 'Quotation'),
    ('d', 'Draft'),
    ('c','Confirmed'),
    ('so', 'Sale Order'),
   
    
  
)

class SaleOrder(models.Model):
    
    ref = models.CharField(max_length=25,blank=True,null=True)
    customer = models.ForeignKey(Customer,related_name="sale_orders",on_delete=models.CASCADE)
    order_date = models.DateField()
    created_date = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS,default='q',max_length=2)
    total_price = models.FloatField(blank=True,null=True)

    def sale_order_total(self):
        total = 0
        for so_line in self.so_lines.all():
            subtotal = so_line.sub_total
            total += subtotal
        return total

    class Meta:
       

        verbose_name = 'SaleOrder'
        verbose_name_plural = 'SaleOrders'

    def __str__(self):
        return self.ref
    
    
    

       




class SaleOrderLine(models.Model):
    sale_order = models.ForeignKey(SaleOrder,related_name="so_lines",on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name="so_lines",on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    # price = models.FloatField()
    sub_total = models.FloatField(blank=True,null=True)


    def get_subtotal(self):
        return self.quantity * self.product.sale_price


     

    class Meta:
        
        verbose_name = 'SaleOrderLine'
        verbose_name_plural = 'SaleOrderLines'
        unique_together = ('sale_order', 'product')

    def __str__(self):
        return self.sale_order.ref
       


