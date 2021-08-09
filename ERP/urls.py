"""ERP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
 
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls")) ,            # UI Kits Html files

    #Customer URL COnfig
    # path("customer/",include('customer.urls')),
    path('customer/',include('customer.urls',namespace="customer")),
    path('product/',include('product.urls',namespace="product")),
    path('sale/',include('sale.urls',namespace="sale")),
    path('inventory/',include('inventory.urls',namespace="inventory")),
    path('purchase/',include('purchase.urls',namespace="purchase")),

    




    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)