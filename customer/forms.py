from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import CheckboxInput
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import Customer


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

    # def save(self,commit=True):
    #     m = super(CustomerForm, self).save(commit=False)
    #     if m:
    #         print("Save method called")
    #         username = self.cleaned_data.get('name')
    #         email = self.cleaned_data.get('email')
    #         password = self.cleaned_data.get('password1')
    #         address = self.cleaned_data.get('address')
    #         country = self.cleaned_data.get('country')
    #         image = self.cleaned_data.get('image')
    #         country = self.cleaned_data.get('country')


    #         user = User.objects.get_or_create(username=username,email=email,password=password)
    #         user[0].set_password(password)
    #         user[0].save()
    #         customer= Customer.objects.get(user=user[0])
    #         customer.name = username
    #         customer.address = address
    #         customer.country=country
    #         customer.image = image
    #         customer.email = email
    #         customer.save()
    #         return m






        

       
        
