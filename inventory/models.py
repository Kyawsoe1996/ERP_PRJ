from django.db import models
from django.urls import reverse

# Create your models here.


class Warehouse(models.Model):
    

    name = models.CharField(max_length=50)

    class Meta:
     

        verbose_name = 'Warehouse'
        # verbose_name_plural = 'Warehouses'

    def __str__(self):
        return self.name

    
    def get_absolute_url(self):
        return reverse('warehouse-detail', kwargs={'pk': self.pk})
