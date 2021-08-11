from django.http.response import HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
# from inventory.models import Warehouse
from django.utils import timezone
from django.urls import reverse_lazy
from django import forms


# Create your views here.

def invoice_view(request):
    return HttpResponse("Invoice")
    