from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication, permissions

#generic filter
from rest_framework import generics
import django_filters.rest_framework

#searchFilter
from rest_framework import filters
#custom search overide backends
#from .backends import CustomSearchFilter

#pagination
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

#viewset

#for customm issue book
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import serializers
import datetime

