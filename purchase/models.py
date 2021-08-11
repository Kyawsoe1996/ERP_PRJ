from django.db import models
from django.db.models.fields import related
from customer.models import Customer
from product.models import Product
import  datetime
from django.urls import reverse
# from invoice.models import Invoice

# Create your models here.




STATUS = (
    ('q', 'Quotation'),
    ('d', 'Draft'),
    ('c','Confirmed'),
    ('so', 'Purchase Order'),
   
    
  
)

class PurchaseOrder(models.Model):
    
    ref = models.CharField(max_length=25,blank=True,null=True)
    vendor = models.ForeignKey(Customer,related_name="purchase_orders",on_delete=models.CASCADE)
    purchase_date = models.DateField()
    created_date = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS,default='q',max_length=2)
    total_price = models.FloatField(blank=True,null=True)
    # invoice_ids = models.ManyToManyField(Invoice,blank=True)

    def purchase_order_total(self):
        total = 0
        for po_line in self.po_lines.all():
            subtotal = po_line.sub_total
            total += subtotal
        return total

    class Meta:
       

        verbose_name = 'PurchaseOrder'
        verbose_name_plural = 'PurchaseOrders'

    def __str__(self):
        return self.vendor.name

    def get_absolute_url(self):
        return reverse('purchase-detail', kwargs={'pk': self.pk})

    
    
    

       




class PurchaseOrderLine(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder,related_name="po_lines",on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name="po_lines",on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    # price = models.FloatField()
    sub_total = models.FloatField(blank=True,null=True)


    def get_subtotal(self):
        return self.quantity * self.product.purchase_price


     

    class Meta:
        
        verbose_name = 'PurchaseOrderLine'
        verbose_name_plural = 'PurchaseOrderLines'
        unique_together = ('purchase_order', 'product')

    def __str__(self):
        return self.purchase_order.vendor.name