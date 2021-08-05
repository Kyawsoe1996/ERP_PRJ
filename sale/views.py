from django.shortcuts import redirect, render
from django.http import HttpResponse
from sale.forms import SaleOrderForm,SaleOrderLineFormSet
from sale.models import SaleOrder,SaleOrderLine
import datetime
from django.forms import inlineformset_factory
# Create your views here.

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
            so_form_obj  = so_form.save(commit=False)
            so_form_obj.ref = create_so_num()
            so_form_obj.save()
            for form in formset:
                
                so_line_obj = form.save(commit=False)
                so_line_obj.sale_order = so_form_obj
                so_line_obj.save()
        else:
            return HttpResponse("Something went wrong with your form")
                
               

           

             
            
            

        return HttpResponse("post method called")
        
        
    
    
    # return HttpResponse("CReate SO Page")