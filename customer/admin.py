from django.contrib import admin

# Register your models here.
from .models import Customer,Addr

admin.site.register(Customer)




class AdresssAdmin(admin.ModelAdmin):
    list_display = ['customer',
                    'street_address',
                    'apartment_address',
                    'country',
                    'zip',
                    'address_type',
                    'default']
    list_filter = ['default',
                   'address_type',
                   'country',
                   ]

    search_fields= ['customer__name','street_address','apartment_address','zip']
admin.site.register(Addr,AdresssAdmin)