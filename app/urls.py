# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

    path("button/",views.button,name="button"),
    path("badges/",views.badges,name="badges"),
    path("breadcrumb/",views.breadcrumb,name="breadcrumb"),
    path("collapse/",views.collapse,name="collapse"),
    path("tabs/",views.tabs,name="tabs"),
    path("typography/",views.typography,name="typography"),
    path("icons/",views.icons,name="icons"),
    path("form_element/",views.form_element,name="form_element"),
    path("table/",views.table,name="table"),
    path("charts_morris/",views.charts_morris,name="charts_morris"),
    path("google_map/",views.google_map,name="google_map"),

    path("auth_reset/",views.auth_reset,name="auth_reset"),
    path("register_fn/",views.register_fn,name="register_fn"),
    path("login_fn/",views.login_fn,name="login_fn"),
    path("blank_page/",views.blank_page,name="blank_page"),
    path("page_404/",views.page_404,name="page_404"),


    


    


    








]
