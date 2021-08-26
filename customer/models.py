from django.db import models
from django.db.models.base import Model
from django_countries.fields import CountryField
from django.shortcuts import reverse
from django.contrib.auth.models import User
# Create your models here.

from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token
from django.conf import settings


ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

class Customer(models.Model):
    
    user = models.OneToOneField(User,related_name="customer", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.TextField()
    is_customer = models.BooleanField(default=True)
    is_vendor =models.BooleanField(default=False)
    country = CountryField(multiple=False)
    image = models.ImageField()
    shipping_address = models.ForeignKey(
        'Addr', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'Addr', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)


   

    class Meta:
       

        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
       
        return self.name


    # def get_absolute_url(self):
        
    #     return reverse('customer:customer-detail', kwargs={'id': self.id})
    
    def get_absolute_url(self):
        return reverse('customer:customer-detail', kwargs={'id' : self.id})


@receiver(post_save, sender=User)
def create_customer_when_create_user(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)


#token create import from rest framework Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



#addresss Model
class Addr(models.Model):
    customer = models.ForeignKey(Customer,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=1000)
    apartment_address = models.CharField(max_length=1000)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.name
    
    class Meta:
        verbose_name_plural ='Addresses'

