from django.shortcuts import render
from django.http import HttpResponse
from imp_exp.admin import ProductNameResource
# Create your views here.


def ProductNameExport(request):
    product_name_export = ProductNameResource()
    dataset = product_name_export.export()


    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="productname.csv"'
    return response

    
