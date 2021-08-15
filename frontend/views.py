from django.shortcuts import render

# Create your views here.


def IndexView(request):
    return render(request,"user-frontend/user-ui/index.html")