from django.shortcuts import render
from product.models import Product,ProductCategory
# Create your views here.


def IndexView(request):
    product_lists = Product.objects.all()
    context = {
        "product_lists": product_lists,
       
    }
    return render(request,"user-frontend/user-ui/index.html",context)





   