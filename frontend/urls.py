from django.urls import path,include
from .views import IndexView,GetCategoryRelatedProduct,ProductListView,ProductDetail

app_name="frontend"

urlpatterns = [
    path("", IndexView, name="frontend"),
    path("category/<int:category>/", GetCategoryRelatedProduct, name="category-related-product"),
    path('product-list',ProductListView,name="p-list"),
    path('product/<int:product>/',ProductDetail,name="p-detail"),

    


   

    
]
