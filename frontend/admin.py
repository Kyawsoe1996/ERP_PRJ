from django.contrib import admin

# Register your models here.



class AdresssAdmin(admin.ModelAdmin):
    list_display = ['user',
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

    search_fields= ['user__email','street_address','apartment_address','zip']