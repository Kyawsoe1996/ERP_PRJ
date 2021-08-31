from django.urls import path,include
from .views import(
        PurchaseOrderCreate,
        PurchaseListView,
        PurchaseDetailView,
        PurchaseUpdateView,
        # WarehouseListView,
        # WarehouseCreateView,
        # WarehouseDetailView,
        # WarehouseUpdateView,
        # WarehouseDeleteView,

        CallMethod

) 

app_name="purchase"

urlpatterns = [
    
    path("",PurchaseOrderCreate.as_view(),name="purchase-order"),
    path("list/",PurchaseListView,name="purchase-list"),
    path("detail/<int:pk>/",PurchaseDetailView.as_view(),name="purchase-detail"),
    path("update/<int:pk>/",PurchaseUpdateView.as_view(),name="purchase-update"),

    path('gg/',CallMethod,name="called")

    

    

    # path("warehouse/",WarehouseCreateView.as_view(),name="warehouse"),
    # path('warehouse/<int:pk>/', WarehouseDetailView.as_view(),name='warehouse-detail'),
    # path('warehouse/update/<int:pk>/', WarehouseUpdateView.as_view(),name='warehouse-update'),
    # path('warehouse/delete/<int:pk>/', WarehouseDeleteView.as_view(),name='warehouse-delete'),

    
]