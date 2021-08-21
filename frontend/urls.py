from django.urls import path,include
from .views import IndexView,GetCategoryRelatedProduct,ProductListView,ProductDetail,AddtoCart

app_name="frontend"

urlpatterns = [
    path("", IndexView, name="frontend"),
    path("category/<int:category>/", GetCategoryRelatedProduct, name="category-related-product"),
    path('product-list',ProductListView,name="p-list"),
    path('product/<int:product>/',ProductDetail,name="p-detail"),
    path('add-to-cart/<int:product>/',AddtoCart,name="add-to-cart"),


    


   

    
]
