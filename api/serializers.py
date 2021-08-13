from django.db.models import fields
from django.db.models.query import QuerySet

from rest_framework import serializers
from django.contrib.auth.models import User
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response

from rest_framework.validators import UniqueValidator
from rest_framework import parsers