from django.urls import  path,include

from rest_framework.authtoken import views
#router for viewset
from rest_framework.routers import DefaultRouter
# from .views import 
    # )


# router = DefaultRouter()

app_name = "api"


urlpatterns = [
     path('customer/',include('api.customer.urls','customer_api')),
    


    
]
# router.register(r'books', BookViewSet, basename='book')
