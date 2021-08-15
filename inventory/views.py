from django.http.request import HttpRequest
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


    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(LocationCreateView, self).get_form(form_class)
        for i in form.fields:
            form.fields[i].widget.attrs.update({'class':'form-control'})
        form.fields['name'].label = "Enter Name:"
        form.fields['warehouse_id'].empty_label = "Select Warehouse"

        # form.fields['name'].widget = forms.TextInput(attrs={'placeholder': 'Enter name','class':'form-control'})
        return form
    
    


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
        csv_file = self.request.FILES['csv_file']
        df = pd.read_csv (csv_file)

    
        skipped_row = []
        total_create_stock_count = 0
        for index, row in df.iterrows():
            stock_obj = Stock.objects.filter(location_id__name=row['Location'],product_id__name=row['Product'])
            if stock_obj.exists():
                row["issues"] = 'Stock ALready Exist'
                skipped_row.append(row)
                continue
            else:
                try:
                    product_obj = Product.objects.get(name=row['Product'])
                except:
                    row["issues"] = 'Product Name Wrong'
                    skipped_row.append(row)
                    continue
                    #location
                try:
                    location_obj = Location.objects.get(name=row['Location'])
                    
                except:
                    row["issues"] = "Location Name Wrong"
                    skipped_row.append(row)
                    continue


               
                if location_obj.products.filter(id=product_obj.id).exists():
                    Stock.objects.create(location_id=location_obj,product_id=product_obj,quantity=row['quantity'])
                    total_create_stock_count +=1
                else:
                    row["issues"] =  "Pls add the product in location %s" %  location_obj.name
                    skipped_row.append(row)
                    continue

                        
        
        if len(skipped_row) > 0:
            mydataFrame = pd.DataFrame(skipped_row)
            print(mydataFrame)
            desktop = os.path.join(os.environ.get("HOME"), "Desktop/skipped_stock_import.xlsx")
            
            mydataFrame.to_excel(desktop, index = False, header=True) 
            messages.info(self.request,"Skipped product list can found in Desktop") 
          

           
          
      
        # return redirect("inventory:location-list")
        return super(StockUploadCreateView, self).form_valid(form)
        
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(StockUploadCreateView, self).get_form(form_class)
        for i in form.fields:
            form.fields[i].widget.attrs.update({'class':'form-control'})
       
        # form.fields['warehouse_id'].empty_label = "Select Warehouse"

        # form.fields['name'].widget = forms.TextInput(attrs={'placeholder': 'Enter name','class':'form-control'})
        return form
        






