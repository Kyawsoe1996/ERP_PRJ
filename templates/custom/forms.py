from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import CheckboxInput
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from customer.models import Customer


class CustomerForm(forms.ModelForm):
    """Form definition for Book."""
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Enter password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm password"}))


    class Meta:
        """Meta definition for Bookform."""

        model = Customer
       
        fields = ['name','email','address','country','image','is_customer','is_vendor']
        widgets = {'country': CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-200',
        })}
        widgets = {'is_customer':CheckboxInput()}
        widgets = {'is_vendor':CheckboxInput()}

        
    def __init__(self, *args, **kwargs):
        
        super(CustomerForm,self).__init__(*args, **kwargs)
        if  not self.instance.id is None:
            self.fields.pop('password1')
            self.fields.pop('password2')
            self.fields.pop('is_customer')
            self.fields.pop('is_vendor')
        # self.fields['author'].empty_label = "Select Author"
        self.fields['name'].widget.attrs['placeholder'] = self.fields['name'].label 
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label
        self.fields['address'].widget.attrs['placeholder'] = "Enter your full address"
        self.fields['image'].widget.attrs['placeholder'] = "Image"
       

        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':'form-control'})
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if not password1 == password2:
            msg = "The two password should be match"
            self.add_error('password1',msg)
            self.add_error('password2',msg)








        

       
        
