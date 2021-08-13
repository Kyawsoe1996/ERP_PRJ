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
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.schemas.coreapi import AutoSchema

from rest_framework.routers import DefaultRouter

from rest_framework import routers

router = DefaultRouter()
from rest_framework.schemas.coreapi import AutoSchema

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
    path('invoice/',include('invoice.urls',namespace="invoice")),
    path('ie/',include('imp_exp.urls',namespace="imp-exp")),

    #ALL-API
    path('api/',include('api.urls',namespace="api")),

    #REST FRAMEWORK
    #Add later
    # path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    # path(r'', include(router.urls)),

    #OPENAPIdocs
    path('docs/',include_docs_urls(title="ERP API")),
    path('schema/', get_schema_view(
        title="ERP API LIST",
        description="API for all things …",
        version="1.0.0"
     ), name='openapi-schema'),

   
  




    




    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)