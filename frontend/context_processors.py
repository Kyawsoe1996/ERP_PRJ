from product.models import ProductCategory
from sale.models import SaleOrder,SaleOrderLine
from customer.models import Addr, Customer
from django.contrib.auth.models import User
from customer.models import Addr

def config(request):
    #returning parent category
    categories = ProductCategory.objects.filter(category_parent__isnull=True)
    

    value = 0
    if not request.user.is_authenticated:
        return {'categories':categories,"cart_count":0}
    else:
        try:
            customer_obj = Customer.objects.get(user=request.user)
        except:
            return {'categories':categories,"cart_count":0}


        qs = SaleOrder.objects.filter(customer=customer_obj, status='q')
        if qs.exists():
            value= qs[0].so_lines.all()
            #to get in the Checkout Page ... mean => Checkout Page
            so_obj = qs[0]


         
            
    
    
    
    

    return {'categories':categories,"cart_count":value,"so":so_obj}
