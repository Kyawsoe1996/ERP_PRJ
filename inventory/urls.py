from django.urls import path,include
from .views import(
        WarehouseListView,
        WarehouseCreateView,
        WarehouseDetailView,
        WarehouseUpdateView,
        WarehouseDeleteView,

        #Location
        LocationListView,
        LocationCreateView

) 

app_name="inventory"

urlpatterns = [
    
    path("warehouse/list",WarehouseListView.as_view(),name="warehouse-list"),

    path("warehouse/",WarehouseCreateView.as_view(),name="warehouse"),
    path('warehouse/<int:pk>/', WarehouseDetailView.as_view(),name='warehouse-detail'),
    path('warehouse/update/<int:pk>/', WarehouseUpdateView.as_view(),name='warehouse-update'),
    path('warehouse/delete/<int:pk>/', WarehouseDeleteView.as_view(),name='warehouse-delete'),


    #location
    path("location/list",LocationListView,name="location-list"),
    
    path("location/",LocationCreateView.as_view(),name="location"),


]