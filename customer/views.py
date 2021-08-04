from customer.models import Customer
from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from customer.forms  import CustomerForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def CustomerView(request,id=0):

    if request.method == "GET":
        if id == 0:
            form =CustomerForm()
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(instance=customer)
        return render(request,"customer/index.html",{"form":form})
    else:
        if id==0:
            form = CustomerForm(request.POST,request.FILES)
            if form.is_valid():
                username = form.cleaned_data.get('name')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password1')
                address = form.cleaned_data.get('address')
                country = form.cleaned_data.get('country')
                image = form.cleaned_data.get('image')
                country = form.cleaned_data.get('country')
                is_customer = form.cleaned_data.get('is_customer')
                is_vendor = form.cleaned_data.get('is_vendor')

                user = User.objects.get_or_create(username=username,email=email,password=password)
                user[0].set_password(password)
                user[0].save()
                customer= Customer.objects.get(user=user[0])
                customer.name = username
                customer.address = address
                customer.country=country
                customer.image = image
                customer.email = email
                customer.is_customer = is_customer
                customer.is_vendor = is_vendor
                customer.save()
                return redirect("customer:customer-lists")
            else:
                #if form is invalid, e.g after checking  the two passwords does not match
                context = {"form":form}
                return render(request,"customer/index.html",context)
                

        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(request.POST,request.FILES, instance=customer)
            user = User.objects.get(id=form.instance.user.id)
            user.username =  form.data['name']
            user.email =  form.data['email']
            user.save()
            
            if form.is_valid():
               
                form.save()
                return redirect("customer:customer-lists")
        
def Customerlist(request):
    customer_lists = Customer.objects.all()
    context= {
        "customer_lists":customer_lists
    }
    return render(request,"customer/customer-list.html",context)


def CustomerDetail(request,id):
    try:
        customer_obj = Customer.objects.get(pk=id)
    except:
        context = {
            "page":"Customer Detail",
            "detail":"Customer detail can't found"
        }
        return render(request,"page-404.html",context)
    
    context = {
        "customer":customer_obj
    }
    return render(request,"customer/customer-detail.html",context)

def CustomerDelete(request,id):
   customer = Customer.objects.get(pk=id)
   user = User.objects.get(id=customer.user.id)
   user.delete()
#    customer.delete()
   return redirect("customer:customer-lists")





   


