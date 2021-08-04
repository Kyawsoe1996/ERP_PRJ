from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import CheckboxInput
from django_countries.fields import CountryField

from .models import Product,ProductCategory,ProductUOM

#Product Category
class ProductCategroyForm(forms.ModelForm):
    

    class Meta:
        

        model = ProductCategory
        fields = ['name']
    
    def __init__(self,*args, **kwargs):
        super(ProductCategroyForm,self).__init__(*args, **kwargs)

        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':'form-control'})
        self.fields['name'].widget.attrs['placeholder'] = "Enter Category Name"
        


class ProductUOMForm(forms.ModelForm):
    

    class Meta:
        

        model = ProductUOM
        fields = ['name']
    
    def __init__(self,*args, **kwargs):
        super(ProductUOMForm,self).__init__(*args, **kwargs)

        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':'form-control'})
        self.fields['name'].widget.attrs['placeholder'] = "Enter UOM Name"


