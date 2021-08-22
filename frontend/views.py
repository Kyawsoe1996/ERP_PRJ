from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from product.models import Product,ProductCategory
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from customer.models import Customer
from sale.models import SaleOrder,SaleOrderLine
import datetime
#method for creating ref number 
from sale.views import  create_so_num
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
 
    return JsonResponse({"data":"Add to Cart Called"})

def BuyProduct(request,product):

   

    if not request.user.is_authenticated:
        return JsonResponse({"error":"Login First"})
 
    product_id = request.POST.get('productid')
    qty = request.POST.get('quantity')
    qty = int(qty)

    
    product_id = int(product_id)

    product_obj = Product.objects.get(id=product_id)


    user_obj = request.user
    try:
        customer_obj = Customer.objects.get(user=user_obj)
    except:
        return JsonResponse({"error":"The requested customer does not exist in db"})
    so_obj = SaleOrder.objects.get_or_create(customer=customer_obj,order_date=datetime.datetime.today())
    so_obj = so_obj[0]
    so_obj.ref = create_so_num()
    so_obj.save()
   
    

    so_line_obj = SaleOrderLine.objects.filter(sale_order=so_obj,product=product_obj)
    print(so_line_obj)
    if so_line_obj.exists():
        so_line_obj= so_line_obj[0]
        so_line_obj.quantity += qty
        so_line_obj.sub_total = so_line_obj.get_subtotal()

        so_line_obj.save()

        #update the sale order total price in Sale order object
        so_obj = so_line_obj.sale_order
        so_obj.total_price = so_obj.sale_order_total()
        so_obj.save() 
        return JsonResponse({"data":"Already Exist and Quantity Updated"})
    else:
        so_line_obj = SaleOrderLine.objects.create(sale_order=so_obj,product=product_obj,quantity=qty)
        so_line_obj.sub_total = so_line_obj.get_subtotal()
        so_line_obj.save()

        #update the sale order total price in Sale order object
        
        so_obj = so_line_obj.sale_order
        so_obj.total_price = so_obj.sale_order_total()
        so_obj.save()


        

        #updating on the cart Navbar Count

         



    return JsonResponse({"data":"created","count":1})

        
        

   
    






   