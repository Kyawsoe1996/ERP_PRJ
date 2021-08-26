from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import JsonResponse,HttpResponse
from django.shortcuts import redirect, render
from product.models import Product,ProductCategory
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from customer.models import Customer
from sale.models import SaleOrder,SaleOrderLine
import datetime
#method for creating ref number 
from sale.views import  create_so_num
# Create your views here.
import json 


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
        return JsonResponse({"error":"Not a Customer"})
    # so_obj = SaleOrder.objects.get_or_create(customer=customer_obj,order_date=datetime.datetime.today())
    #filter by customer n status, not by date, if SO need to crete order date, so passing just 
    # https://stackoverflow.com/questions/13610896/django-get-or-create-how-to-say-commit-false
    defaults = {'order_date': datetime.datetime.today()}
    so_obj = SaleOrder.objects.get_or_create(customer=customer_obj,status='q',defaults=defaults)

    so_obj = so_obj[0]
    so_obj.ref = create_so_num()
    so_obj.save()
   
    

    so_line_obj = SaleOrderLine.objects.filter(sale_order=so_obj,product=product_obj)
    print(so_line_obj)
    if so_line_obj.exists():
        so_line_obj= so_line_obj[0]
        # so_line_obj.quantity += qty
        # so_line_obj.sub_total = so_line_obj.get_subtotal()

        # so_line_obj.save()

        # #update the sale order total price in Sale order object
        # so_obj = so_line_obj.sale_order
        # so_obj.total_price = so_obj.sale_order_total()
        # so_obj.save()
        qty_updated = so_line_obj.quantity +  qty
        so_line_obj.add_to_cart_update_qty_and_subtotal_so_price(qty=qty_updated)
        return JsonResponse({"data":"Qty Updated"})
    else:
        so_line_obj = SaleOrderLine.objects.create(sale_order=so_obj,product=product_obj,quantity=qty)
        so_line_obj.add_to_cart_update_qty_and_subtotal_so_price(qty=qty)
        
        
        # so_line_obj.sub_total = so_line_obj.get_subtotal()
        # so_line_obj.save()

        # #update the sale order total price in Sale order object
        
        # so_obj = so_line_obj.sale_order
        # so_obj.total_price = so_obj.sale_order_total()
        # so_obj.save()


        

        #updating on the cart Navbar Count,So i return count to the client

         



    return JsonResponse({"data":"created","count":1})


def ViewAddtoCartItem(request):

    return render(request,"user-frontend/user-ui/view_add_to_cart.html")




def UpdateCart(request):
    #products getting from ajax is JSON STRINGFY, so need to change python object
    product_and_qty_json_lists = request.POST['products']
    product_n_qty_dict = json.loads(product_and_qty_json_lists)

    user_obj = request.user
    try:
        customer_obj = Customer.objects.get(user=user_obj)
    except:
        return JsonResponse({"error":"Not a Customer"})
    
    try:
        so_obj = SaleOrder.objects.get(customer=customer_obj,status='q')
    except:
        return JsonResponse({"error":"Customer does not have Active So"})
    

    print(so_obj.so_lines.all(),'####################')
    
    

    for so_line in so_obj.so_lines.all():
       for product_n_qty in product_n_qty_dict:
           for key,value in product_n_qty.items():
                if int(key) == so_line.product.id:
                  
                  
                  
                  
                  so_line.add_to_cart_update_qty_and_subtotal_so_price(qty=int(value))
                #   so_line.quantity = int(value)
                #   so_line.sub_total = so_line.get_subtotal()
                #   so_line.save()





    
    data ={"success":1,"message":"Cart Updated"}
    return JsonResponse(data)
    

def RemovefromCart(request,product):

    product_obj = Product.objects.get(id=product)
    
    user_obj = request.user
    try:
        customer_obj = Customer.objects.get(user=user_obj)
    except:
        return JsonResponse({"error":"Not a Customer"})
    
    try:
        so_obj = SaleOrder.objects.get(customer=customer_obj,status='q')
    except:
        return JsonResponse({"error":"Customer does not have Active So"})

    

    so_line_obj = so_obj.so_lines.filter(product=product_obj)
    so_line_obj[0].remove_from_cart()

    


    
    


    return redirect("frontend:view-cart")

        
        

   
    






   