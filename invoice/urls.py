from django.urls import path,include
from .views import (
    invoice_view
)
      

app_name="invoice"

urlpatterns = [
    
    path("",invoice_view,name="invoice-base"),

]