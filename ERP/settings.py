"""
Django settings for ERP project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from ERP.ERP import urls
from pathlib import Path
import os
from django.core.exceptions import ImproperlyConfigured
import environ
env = environ.Env()
environ.Env.read_env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# def get_env_variable(var_name):
#     try:
#         return os.environ[var_name]
#     except KeyError:
#         error_msg = "set the %s environment variable" % var_name
#         raise ImproperlyConfigured(error_msg)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b50@c_pa%qz$#y@-m1-b(dvsar@j9*g1((42m16a0#hly^+jl6'
# SECRET_KEY = get_env_variable('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS =[]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'crispy_forms',
    'django_countries',
    'app',
    'authentication',
    'customer',
    'vendor',
    'product',
    'sale',
    'inventory',
    'purchase',
    'django_extensions',
    'django_htmx',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'

]

ROOT_URLCONF = 'ERP.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ERP.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#local
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'erp_project',
        'USER': 'postgres',
        'PASSWORD': 'shamu',
        'HOST': 'localhost'
    }
}

# postgres://uvkhnnygrudhid:d4e66234b91b9c905b8ff55ec9de3f14f7086c17b68e512952ecca919c2331ee@ec2-34-204-128-77.compute-1.amazonaws.com:5432/d9evm2d96p0tno

# For Heroku Production
# DATABASES = {
#     # 'default': {
#     #     'ENGINE': 'django.db.backends.sqlite3',
#     #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     # }
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'd9evm2d96p0tno',
#         'USER': 'uvkhnnygrudhid',
#         'PASSWORD': 'd4e66234b91b9c905b8ff55ec9de3f14f7086c17b68e512952ecca919c2331ee',
#         'HOST': 'ec2-34-204-128-77.compute-1.amazonaws.com',
#         'PORT': 5432,
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]







# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True






# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_in_venv/')

#for media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

