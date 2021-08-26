from django.contrib import admin

# Register your models here.
from .models import Customer,Addr

admin.site.register(Customer)
admin.site.register(Addr)