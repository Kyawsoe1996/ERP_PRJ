from django.db import models

from django.shortcuts import reverse
# for barcode generation
import barcode                      # additional imports
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File

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
    

    class Meta:
        

        verbose_name = 'ProductCategory'
        verbose_name_plural = 'ProductCategories'

    def __str__(self):
        return self.name


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


    class Meta:
        

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
       return self.name
    
    def get_absolute_url(self):
        
        return reverse('product:product-detail', kwargs={'id': self.id})

    def save(self, *args, **kwargs):          # overriding save() 
        COD128 = barcode.get_barcode_class('code128')
        rv = BytesIO()
        code = COD128(f'{self.name}', writer=ImageWriter()).write(rv)
        self.barcode.save(f'{self.name}.png', File(rv), save=False)
        return super().save(*args, **kwargs)
