# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    # import pdb;pdb.set_trace()
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

def button(request):
    return render(request,"ui-button.html")

def badges(request):
    return render(request,"ui-badges.html")
def breadcrumb(request):
    return render(request,"ui-breadcrumb-pagination.html")

def collapse(request):
    return render(request,"ui-collapse.html")


def tabs(request):
    return render(request,"ui-tabs.html")

def typography(request):
    return render(request,"ui-typography.html")

def icons(request):
    return render(request,"ui-icons.html")


def form_element(request):
    return render(request,"ui-forms.html")

def table(request):
    return render(request,"ui-tables.html")

def charts_morris(request):
    return render(request,"charts-morris.html")


def google_map(request):
    return render(request,"maps-google.html")


def auth_reset(request):
    return render(request,"auth-reset-pass.html")



def login_fn(request):
    return render(request,"login.html")



def register_fn(request):
    return render(request,"register.html")




def blank_page(request):
    return render(request,"page-blank.html")


def page_404(request):
    return render(request,"page-404.html")











