from django.urls import path,include
from .views import (
   create_so,
   frontend,
   SOListView,
   SODetialView,
)
app_name="sale"

urlpatterns = [
    path("",create_so,name="create-so"),
    path("fr",frontend,name="frontend"),
    path("list/",SOListView,name="so-list"),
    path("detail/<int:id>/",SODetialView,name="so-detail"),

    

 



    

    
 
    
]
