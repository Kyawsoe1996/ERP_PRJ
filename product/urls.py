from django.urls import path,include
from .views import (
    ProductCategoryView,
    CategoryList,
    CategoryDetail,
    CategoryDelete,

    #product-uom
    ProductUOMView,
    UOMList,
    UOMDetail,
    UOMDelete,

    ProductView,
    ProductList,
    ProductDetail,
    ProductDelete,
    
)
app_name="product"

urlpatterns = [
    path("category/",ProductCategoryView,name="product-category"),
    path("category/list/",CategoryList,name="product-category-list"),
    # path('<int:id>/',ProductCategoryView,"category-update"),
    path('category/<int:id>/', ProductCategoryView,name='category-update'),
    path('category/detail/<int:id>/',CategoryDetail,name="category-detail"),
    path('category/delete/<int:id>/',CategoryDelete,name="category-delete"),





    path("uom/",ProductUOMView,name="product-uom"),
    path("uom/list",UOMList,name="uom-list"),
    path('uom/<int:id>/', ProductUOMView,name='uom-update'),
    path('uom/detail/<int:id>/',UOMDetail,name="uom-detail"),
    path('uom/delete/<int:id>/',UOMDelete,name="uom-delete"),





    


    path("",ProductView,name="product"),
    path("list/",ProductList,name="product-list"),
    path('<int:id>/', ProductView,name='product-update'),
    path('detail/<int:id>/',ProductDetail,name="product-detail"),
    path('delete/<int:id>/',ProductDelete,name="product-delete"),




    

    
    # path("", CustomerView, name="cus"),
    # path('<int:id>/', CustomerView,name='customer-update'),
    # path('list/',Customerlist,name="customer-lists"),
    # path('detail/<int:id>/',CustomerDetail,name="customer-detail"),
    # path('delete/<int:id>/',CustomerDelete,name="customer-delete"),

    
]
