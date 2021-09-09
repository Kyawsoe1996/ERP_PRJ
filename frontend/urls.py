from django.urls import path,include
from django.contrib.auth.decorators import login_required

from .views import (
    IndexView,
    GetCategoryRelatedProduct,
    ProductListView,
    ProductDetail,
    AddtoCart,
    BuyProduct,
    ViewAddtoCartItem,
    UpdateCart,
    RemovefromCart,
    CheckoutView,
    SearchView,
    VendorDetailView,
)

app_name="frontend"

urlpatterns = [
    path("", IndexView, name="frontend"),
    path("category/<int:category>/", GetCategoryRelatedProduct, name="category-related-product"),
    path('product-list',ProductListView,name="p-list"),
    path('product/<int:product>/',ProductDetail,name="p-detail"),
    path('add-to-cart/<int:product>/',AddtoCart,name="add-to-cart"),
    path('buy-product/<int:product>/',BuyProduct,name="buy-product"), #create so and qty update
    path('cart/',ViewAddtoCartItem,name="view-cart"),
    path('update-cart/',UpdateCart,name="update-cart"),
    path('removefromcart/<int:product>/',RemovefromCart,name="remove-from-cart"),
    path('checkout/',CheckoutView.as_view(),name="checkout-view"),
    path('search/',SearchView,name="search-view"),
    path('vendor/<int:id>/',VendorDetailView.as_view(),name="vendor-detail"),












    


   

    
]
