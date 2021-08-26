from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)

class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    billing_zip = forms.CharField(required=False)

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    # payment_option = forms.ChoiceField(
    #     widget=forms.RadioSelect(attrs={
    #         'class':'custom-control-input',
    #     }), choices=PAYMENT_CHOICES)

    def __init__(self,*args, **kwargs):
        super(CheckoutForm,self).__init__(*args, **kwargs)

        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':'form-control'})
       


class CouponForm(forms.Form):
    
    code = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Promo Code',
        'class':'form-control',
        'aria-label':"Recipient's username",
        'aria-describedby':'basic-addon2'

    }))