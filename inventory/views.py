from product.models import Product
from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from inventory.models import Warehouse,Location,StockUpload,Stock
from django.utils import timezone
from django.urls import reverse_lazy
from django import forms
import csv

import pandas as pd
import os


class WarehouseListView(ListView):

    model = Warehouse
    # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class WarehouseCreateView(CreateView):
    model = Warehouse
    fields = ['name','vendor']
    success_message = "New student successfully added."
    success_url = reverse_lazy('inventory:warehouse-list')


    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(WarehouseCreateView, self).get_form(form_class)
        for i in form.fields:
            form.fields[i].widget.attrs.update({'class':'form-control'})

        form.fields['vendor'].empty_label = "Select Vendor"

        form.fields['name'].widget = forms.TextInput(attrs={'placeholder': 'Enter name','class':'form-control'})
        return form



class WarehouseDetailView(DetailView):
    model = Warehouse
    template_name = "inventory/warehouse_detail.html"


class WarehouseUpdateView(UpdateView):
    model = Warehouse
    fields = ['name','vendor']
    success_url = reverse_lazy('inventory:warehouse-list')


    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(WarehouseUpdateView, self).get_form(form_class)
        for i in form.fields:
            form.fields[i].widget.attrs.update({'class':'form-control'})
        form.fields['name'].widget = forms.TextInput(attrs={'placeholder': 'Enter name','class':'form-control'})
        return form





    


class WarehouseDeleteView(DeleteView):
    model = Warehouse
    success_url = reverse_lazy('inventory:warehouse-list')

   



def InventroyView(request):
    return HttpResponse("Inventory View Called")




def LocationListView(request):
    return render(request,"location/list.html")


class LocationCreateView(CreateView):
    model = Location
    template_name = 'location/location_form.html'
    fields = ['name','warehouse_id','product_name_csv_file']
    success_message = "Location successfully added."
    success_url = reverse_lazy('inventory:location-list')


    def form_valid(self, form):
        context = self.get_context_data()
        csv_file = self.request.FILES['product_name_csv_file']
       
        product_lists = []
        df = pd.read_csv (csv_file)
        for i in  df['name']:
            product_lists.append(i)
        location_obj = form.save()
        

        
        skipped_data = []
        #check all the product exit in database
        for product_name in product_lists:
            try:
                product = Product.objects.get(name=product_name)
                location_obj.products.add(product)
            except:
               
                skipped_data.append(product_name)
        
        
        location_obj.save()

        
        if len(skipped_data) == 0:
            return super(LocationCreateView, self).form_valid(form)
        mydataFrame = pd.DataFrame()
        dict = {
            "name":skipped_data
        }
        mydataFrame = pd.DataFrame(dict)
        
        desktop = os.path.join(os.environ.get("HOME"), "Desktop/wrong_product.xlsx")
        mydataFrame.to_excel(desktop, index = False, header=True)

        messages.info(self.request,"Wrong data in the  Desktop... Check")

        return redirect("/")
        
       


    # def get_form(self, form_class=None):
    #     if form_class is None:
    #         form_class = self.get_form_class()
    #     form = super(LocationCreateView, self).get_form(form_class)
    #     for i in form.fields:
    #         form.fields[i].widget.attrs.update({'class':'form-control'})

    #     form.fields['vendor'].empty_label = "Select Vendor"

    #     form.fields['name'].widget = forms.TextInput(attrs={'placeholder': 'Enter name','class':'form-control'})
    #     return form



class StockUploadCreateView(CreateView):
    model = StockUpload
    template_name = 'stock/stock_form.html'
    fields = ['csv_file']
    success_message = "Stock successfully added."
    success_url = reverse_lazy('inventory:location-list')


    def form_valid(self, form):
        context = self.get_context_data()
        import pdb;pdb.set_trace()
        csv_file = self.request.FILES['csv_file']
        df = pd.read_csv (csv_file)
        for index, row in df.iterrows():
            print (row["Product"], row["Location"])
      
        return redirect("inventory:location-list")
        # return super(StockUploadCreateView, self).form_valid(form)
        






