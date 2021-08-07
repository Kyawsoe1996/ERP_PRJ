from django.shortcuts import redirect, render
from django.http import HttpResponse
from sale.forms import SaleOrderForm,SaleOrderLineFormSet
from sale.models import SaleOrder,SaleOrderLine
import datetime
from django.forms import inlineformset_factory
# Create your views here.
from sale.models import STATUS

def create_so_num():
        code = 'SO '
        month =datetime.date.today().month
        day = datetime.date.today().day
        year = datetime.date.today().year
        format_str = "%s/%s/%s---" % (day,month,year)
        
        if SaleOrder.objects.all().count() == 0:
            so_max_id = 0
        else:
            so_max_id = SaleOrder.objects.all().order_by("-id")[0].id
        
        so_code = code + format_str +str(so_max_id + 1)
        return so_code

def create_so(request):
    template_name = 'sale/create_so.html'

    if request.method == 'GET':
        so_form = SaleOrderForm(request.GET or None)
        formset = SaleOrderLineFormSet(queryset=SaleOrderLine.objects.none())
        context = {
            "so_form":so_form,
            "formset":formset
        }
        return render(request,template_name,context)
    else:
        so_form = SaleOrderForm(request.POST)
        formset = SaleOrderLineFormSet(request.POST)
        if so_form.is_valid() and formset.is_valid():
            so_obj  = so_form.save(commit=False)
            so_obj.ref = create_so_num()
            so_obj.save()
            for form in formset:
                
                so_line_obj = form.save(commit=False)

                so_line_obj.sale_order = so_obj
                so_line_obj.sub_total = so_line_obj.get_subtotal()
                #unique_together_issue_check

                for so_line in so_obj.so_lines.all():
                    if so_line.product.id == so_line_obj.product.id:
                        return HttpResponse("This %s  already duplicate" % so_line.product.name)


                so_line_obj.save()
            so_obj.total_price = so_obj.sale_order_total()
            so_obj.save()
        else:
            return HttpResponse("Something went wrong with your form")
                
               

           

             
            
            

        return HttpResponse("post method called")

def SOListView(request):
    context = {
        "so_lists":SaleOrder.objects.all()
    }
    return render(request,"sale/list.html",context)


def SODetialView(request,id):
    
    try:
        so_obj = SaleOrder.objects.get(pk=id)
    except:
        context = {
            "page":"Sale Order Detail",
            "detail":"Sale Order detail can't found"
        }
        return render(request,"page-404.html",context)
    
    context = {
        "status":STATUS,
        "so_obj":so_obj
    }
    return render(request,"sale/detail.html",context)

        
        
    
    
  
  
  
  
    # return HttpResponse("CReate SO Page")

def frontend(request):

    return render(request,"frontend/index.html")