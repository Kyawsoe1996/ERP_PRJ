from django.contrib import admin
from .models import Invoice,InvoiceLine
# Register your models here.

admin.site.register(Invoice)
admin.site.register(InvoiceLine)
