from product.forms import ProductUOMForm,ProductCategroyForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
# from .forms import ProductCategroyForm
from product.models import ProductUOM,Product,ProductCategory
# Create your views here.

#Product Category
def ProductCategoryView(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = ProductCategroyForm()
        else:
            category_obj = ProductCategory.objects.get(pk=id)
            form = ProductCategroyForm(instance=category_obj)    
        return render(request,"product_category/index.html",{"form":form})
    else:
        if id ==0 :
            form = ProductCategroyForm(request.POST)
        else:
            category_obj = ProductCategory.objects.get(pk=id)
            form = ProductCategroyForm(request.POST,instance=category_obj)
        if form.is_valid():
            form.save()
            return redirect("product:product-category-list")
        


def CategoryList(request):
    category_lists =  ProductCategory.objects.all()
    context = {
        "category_lists":category_lists
    }
    return render(request,"product_category/list.html",context)

def CategoryDetail(request,id):
    category_obj = ProductCategory.objects.get(pk=id)

    context = {
        "category":category_obj
    }
    return render(request,"product_category/detail.html",context)

def CategoryDelete(request,id):
    category_obj = ProductCategory.objects.get(pk=id)
    category_obj.delete()
    return redirect("product:product-category-list")


#ProductUOM
def ProductUOMView(request,id=0):

    if request.method == "GET":
        if id == 0:
            form = ProductUOMForm()
        else:
            category_obj = ProductUOM.objects.get(pk=id)
            form = ProductUOMForm(instance=category_obj)    
        return render(request,"product_uom/index.html",{"form":form})
    else:
        if id ==0 :
            form = ProductUOMForm(request.POST)
        else:
            category_obj = ProductUOM.objects.get(pk=id)
            form = ProductUOMForm(request.POST,instance=category_obj)
        if form.is_valid():
            form.save()
            return redirect("product:uom-list")


def UOMList(request):
    uom_lists = ProductUOM.objects.all()
    context = {
        "uom_lists":uom_lists
    }
    return render(request,"product_uom/list.html",context)



    

def UOMDetail(request,id):
    uom_obj = ProductUOM.objects.get(pk=id)

    context = {
        "uom":uom_obj
    }
    return render(request,"product_uom/detail.html",context)

def UOMDelete(request,id):
    uom_obj = ProductUOM.objects.get(pk=id)
    uom_obj.delete()
    return redirect("product:uom-list")




#Product
def ProductView(request):
    return render(request,"product/index.html")
    


