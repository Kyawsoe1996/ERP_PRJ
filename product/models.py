# from inventory.models import Stock
from django.db import models

from django.shortcuts import reverse
# for barcode generation
import barcode                      # additional imports
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
from customer.models import Customer

# Create your models here.

TYPE = (
    ('stock', 'Stockable Product'),
    ('consu', 'Consumable'),
    ('service', 'Service')
    
  
)

class ProductUOM(models.Model):
   
    name =models.CharField(max_length=10)
    

    class Meta:
       

        verbose_name = 'ProductUOM'
        verbose_name_plural = 'ProductUOMs'

    def __str__(self):

        return self.name


class ProductCategory(models.Model):
    
    name = models.CharField(max_length=50)
    category_parent = models.ForeignKey('self', blank=True, null=True, related_name='children',on_delete=models.CASCADE)
    class Meta:
        

        verbose_name = 'ProductCategory'
        verbose_name_plural = 'ProductCategories'

    

    def __str__(self):
        return self.name

    def get_children_category(self):
        return self.children.all()


class Product(models.Model):
    
    name = models.CharField(max_length=50)
    type = models.CharField(choices=TYPE,default='stock',max_length=10)
    category = models.ForeignKey(ProductCategory,related_name="products",on_delete=models.CASCADE)
    uom = models.ForeignKey(ProductUOM,related_name="products",on_delete=models.CASCADE)
    image = models.ImageField()
    slug = models.SlugField()
    barcode = models.ImageField(upload_to='barcodes/', blank=True)
    # barcode = models.IntegerField(blank=True,null=True)
    sale_price = models.FloatField(blank=True,null=True)
    purchase_price = models.FloatField(blank=True,null=True)
    vendor = models.ForeignKey(Customer,related_name="products",on_delete=models.CASCADE,blank=True,null=True)


    class Meta:
        

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
       return self.name
    
    def get_absolute_url(self):
        
        return reverse('product:product-detail', kwargs={'id': self.id})

    
    #for just showing on the official store detail vendor page
    def get_10_percent_discount(self):
        percentage = self.sale_price / 10
        new_price =  percentage + self.sale_price   
        return new_price


   

    #getting stock total count product detail page
    def get_total_stock_quantity(self):
        total = 0
        for stock in self.stocks.all():
            total +=  stock.quantity
        return total

    def get_all_location_for_product_and_relative_qty(self):
        # import pdb;pdb.set_trace()
        location_lits = []
        qty_lists = []
        for stock  in self.stocks.all():
            location_obj = stock.location_id
            location_lits.append(location_obj)
            qty_lists.append(stock.quantity)
        
        stock_location_and_its_quantity =list(zip(location_lits, qty_lists))
        
        return stock_location_and_its_quantity

        

    def save(self, *args, **kwargs):          # overriding save() 
        COD128 = barcode.get_barcode_class('code128')
        rv = BytesIO()
        code = COD128(f'{self.name}', writer=ImageWriter()).write(rv)
        self.barcode.save(f'{self.name}.png', File(rv), save=False)
        return super().save(*args, **kwargs)
