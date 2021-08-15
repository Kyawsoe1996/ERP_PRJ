from django.urls import path,include
from .views import IndexView

app_name="frontend"

urlpatterns = [
    path("", IndexView, name="frontend"),
   

    
]
