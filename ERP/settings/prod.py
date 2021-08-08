import os
import environ
from .base import *

# SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
# SECRET_KEY = 'b50@c_pa%qz$#y@-m1-b(dvsar@j9*g1((42m16a0#hly^+jl6'

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS =['mydjangoerpapp.herokuapp.com']


# For Heroku Production
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd9evm2d96p0tno',
        'USER': 'uvkhnnygrudhid',
        'PASSWORD': 'd4e66234b91b9c905b8ff55ec9de3f14f7086c17b68e512952ecca919c2331ee',
        'HOST': 'ec2-34-204-128-77.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'