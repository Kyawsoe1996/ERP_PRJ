from django.db import models
from django.urls import reverse
from product.models import Product
from customer.models import Customer
from  purchase.models import PurchaseOrder
# Create your models here.

STATUS = (
   
    ('d', 'Draft'),
    ('o','Open'),
    ('p', 'Paid'),
   
    
  
)

class Invoice(models.Model):
    ref = models.CharField(max_length=50,blank=True,null=True)
    invoice_date = models.DateField()
    creation_date = models.DateTimeField(auto_now=True)
    invoice_for =  models.ForeignKey(Customer,related_name="invoices",on_delete=models.CASCADE)
    status = models.CharField(max_length=1,choices=STATUS,default='q')
    total_amount = models.FloatField(blank=True,null=True)
    purchase_order = models.ForeignKey(PurchaseOrder,related_name="po_invoices",on_delete=models.CASCADE,blank=True,null=True)

    
    


    class Meta:

        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'

    def __str__(self):
        return self.ref

    # def save(self):
    #     pass

    # def get_absolute_url(self):
    #     return ('')


class InvoiceLine(models.Model):
    
    invoice = models.ForeignKey(Invoice,related_name="invoice_lines",on_delete=models.CASCADE,)
    product = models.ForeignKey(Product, related_name="invoice_lines",on_delete=models.CASCADE)
    price = models.FloatField(blank=True,null=True)
    quantity = models.IntegerField(blank=True,null=True)
    sub_total = models.FloatField(blank=True,null=True)


    class Meta:
        
        verbose_name = 'InvoiceLine'
        verbose_name_plural = 'InvoiceLines'
        unique_together = ('invoice', 'product')




    def __str__(self):
        return self.invoice.ref

   

    


