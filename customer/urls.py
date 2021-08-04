from django.urls import path,include
from .views import CustomerView,Customerlist,CustomerDetail,CustomerDelete

app_name="customer"

urlpatterns = [
    path("", CustomerView, name="cus"),
    path('<int:id>/', CustomerView,name='customer-update'),
    path('list/',Customerlist,name="customer-lists"),
    path('detail/<int:id>/',CustomerDetail,name="customer-detail"),
    path('delete/<int:id>/',CustomerDelete,name="customer-delete"),

    
]
