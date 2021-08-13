from django.urls import  path,include

from rest_framework.authtoken import views
#router for viewset
from rest_framework.routers import DefaultRouter

from api.product.views import ProductViewSet 

router = DefaultRouter()

app_name = "api"


urlpatterns = [
    # path('',custom_view,name="customer-api"),
   

    
]
router.register(r'', ProductViewSet, basename='product')






urlpatterns += router.urls