from django.db.models import query
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import PurchaseOrder,PurchaseOrderLine
from .forms import PurchaseOrderLineForm,PurchaseOrderLineFormSet,PurchaseOrderForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.db import transaction
from django.http import HttpResponse
from django import forms
import datetime
from django.forms import widgets
from .models import STATUS
from product.models import Product
from customer.models import Customer




def create_po_num():
        code = 'PO '
        month =datetime.date.today().month
        day = datetime.date.today().day
        year = datetime.date.today().year
        format_str = "%s/%s/%s---" % (day,month,year)
        
        if PurchaseOrder.objects.all().count() == 0:
            so_max_id = 0
        else:
            so_max_id = PurchaseOrder.objects.all().order_by("-id")[0].id
        
        po_code = code + format_str +str(so_max_id + 1)
        return po_code

def PurchaseListView(request):
    po_lists = PurchaseOrder.objects.all()
    context = {
        "po_lists":po_lists
    }
    return render(request,"purchase/purchase_list.html",context)

class DateInput(forms.DateInput):
    input_type = 'date'

class PurchaseOrderCreate(CreateView):
    model = PurchaseOrder
    template_name = 'purchase/purchase_create.html'
    form_class = PurchaseOrderForm
    # success_url = None
    success_url = reverse_lazy('purchase:purchase-list')


    

   
    def get_context_data(self, **kwargs):
        data = super(PurchaseOrderCreate, self).get_context_data(**kwargs)
        vendor = self.request.GET.get('vendor')
        if vendor is not None:
            vendor = int(vendor)
            print(vendor)
            # vendor = int(vendor)
            # print(vendor,"Integer")
           
            
            customer_obj = Customer.objects.get(id=vendor)
            queryset = Product.objects.filter(vendor=customer_obj)
        
            if self.request.POST:
                data['titles'] = PurchaseOrderLineFormSet(queryset,self.request.POST)
            else:
                if self.request.is_ajax:
                    data['titles'] = PurchaseOrderLineFormSet(queryset)
        else:
            if self.request.POST:
                data['titles'] = PurchaseOrderLineFormSet(self.request.POST)
            else:
            #https://stackoverflow.com/questions/19305964/change-queryset-of-model-field-in-inlineformset-of-non-parent-model 

                queryset = Product.objects.all()
                data['titles'] = PurchaseOrderLineFormSet(queryset)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['titles']
        with transaction.atomic():
            # form.instance.created_by = self.request.user
            self.object = form.save(commit=False)
            self.object.ref = create_po_num()
            self.object.save()
            if titles.is_valid():
                
                for  form in titles:
                    po_line_obj = form.save(commit=False)
                    po_line_obj.sub_total = po_line_obj.get_subtotal()

                    po_line_obj.purchase_order = self.object

                    po_line_obj.save()
                # titles.instance = self.object
                # titles.save()
            self.object.total_price = self.object.purchase_order_total()
            self.object.save()
        return super(PurchaseOrderCreate, self).form_valid(form)



class PurchaseDetailView(DetailView):
    model = PurchaseOrder
    template_name = "purchase/purchase_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PurchaseDetailView, self).get_context_data(**kwargs)
        context['status'] = STATUS
        return context



class PurchaseUpdateView(UpdateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = 'purchase/purchase_create.html'
    success_url = reverse_lazy('purchase:purchase-list')


    def get_context_data(self, **kwargs):
        vendor = self.request.GET.get('vendor')
        print(vendor,"#########")
        data = super(PurchaseUpdateView, self).get_context_data(**kwargs)
        if vendor is not None:
            vendor = int(vendor)
            print(vendor)
            # vendor = int(vendor)
            # print(vendor,"Integer")
           
            
            customer_obj = Customer.objects.get(id=vendor)
            queryset = Product.objects.filter(vendor=customer_obj)
       
            if self.request.POST:
                data['titles'] = PurchaseOrderLineFormSet(queryset,self.request.POST, instance=self.object)
            else:
                data['titles'] = PurchaseOrderLineFormSet(queryset,instance=self.object)
        else:
            if self.request.POST:
                data['titles'] = PurchaseOrderLineFormSet(self.request.POST, instance=self.object)
            else:
                queryset = Product.objects.all()
                data['titles'] = PurchaseOrderLineFormSet(queryset,instance=self.object)
        return data

    


    
    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['titles']
        with transaction.atomic():
            # form.instance.created_by = self.request.user
            self.object = form.save(commit=False)
           
            po_obj = self.object
            self.object.save()
            
            titles.save()
            for po_line in self.object.po_lines.all():
                po_line.sub_total = po_line.get_subtotal()
                po_line.save()
            self.object.total_price = self.object.purchase_order_total()
            self.object.save()
          
        return super(PurchaseUpdateView, self).form_valid(form)


def CallMethod(request):

    print ("Called")
   
    
   
    return JsonResponse({"data":"EZ"})
   