from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from product.models import Product,ProductCategory
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from customer.models import Customer
from sale.models import SaleOrder,SaleOrderLine
import datetime
# Create your views here.


def IndexView(request):
    product_lists = Product.objects.all()
    context = {
        "product_lists": product_lists,
       
    }
    return render(request,"user-frontend/user-ui/index.html",context)


def ProductListView(request):
    product_lists = Product.objects.all()
    context = {
        "product_lists":product_lists
    }

    return render(request,"user-frontend/user-ui/product-list.html",context)

def GetCategoryRelatedProduct(request,category):
    category_lists = ProductCategory.objects.all()[:5]

    try:
        category_obj =  ProductCategory.objects.get(id = category)
    except ObjectDoesNotExist:
        return HttpResponse("Not related category found")
    
    product_lists = Product.objects.filter(category=category_obj)

    context = {
        "product_lists":product_lists,
        "category_lists":category_lists
    }

    return render(request,"user-frontend/user-ui/category_base_product_list.html",context)


    # product_lists = Product.objects.all()
    # data = {
    #     "name":product_lists[0].name,
    #     "category":product_lists[0].category.name,
    #     "image":product_lists[0].image.url,
    #     "slug":product_lists[0].slug
    #     # "name":product_lists[0].name,


    # }
    # return JsonResponse(data)


def ProductDetail(request,product):

    product_obj = get_object_or_404(Product, pk=product)
    product_lists = Product.objects.exclude(id=product)[:3]
    context = {
        "product":product_obj,
        "product_lists":product_lists,
    }

    return render(request,"user-frontend/user-ui/product_detail.html",context)


# @login_required
def AddtoCart(request,product):


    if not request.user.is_authenticated:
        return JsonResponse({"error":"Login First"})
 
    product_id = request.POST.get('productid')

    
    product_id = int(product_id)

    product_obj = Product.objects.get(id=product_id)


    user_obj = request.user
    customer_obj = Customer.objects.get(user=user_obj)
    so_obj = SaleOrder.objects.get_or_create(ref="AJAX",customer=customer_obj,order_date=datetime.datetime.today())
    
    print(so_obj[0].so_lines.all())
    print(so_obj)


    data = {
        "name":product_obj.name,
        "category":product_obj.category.name,
        "sprice":product_obj.sale_price,
        "user":request.user.username
    }

    # raise ValidationError("WEW")

    return JsonResponse(data)
    






   