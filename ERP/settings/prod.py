import os
from .base import *

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
# SECRET_KEY = 'b50@c_pa%qz$#y@-m1-b(dvsar@j9*g1((42m16a0#hly^+jl6'

DEBUG = False
ALLOWED_HOSTS =['mydjangoerpapp.herokuapp.com','127.0.0.1','localhost']