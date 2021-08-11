from django.urls import path,include
from .views import  (
    ProductNameExport
)
       

app_name="imp-exp"

urlpatterns = [
    path("product-name/",ProductNameExport,name="product-name-export"),
]