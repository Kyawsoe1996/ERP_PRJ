from django.urls import  path,include

from rest_framework.authtoken import views
#router for viewset
from rest_framework.routers import DefaultRouter
from .views import custom_view
from api.customer.views import CustomerViewSet 

router = DefaultRouter()

app_name = "api"


urlpatterns = [
    # path('',custom_view,name="customer-api"),
   

    
]
router.register(r'', CustomerViewSet, basename='customer')






urlpatterns += router.urls