"""
Django settings for online_store project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9n)^k+@3$$#bjk8a$cc)6jz$+91br-d)9$68m=pftbk$pbq$od'



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'rest_framework',
    'rest_framework.authtoken',
    'django_extensions',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'online_store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'myapp.context_processors.search_form'
            ],
        },
    },
]

WSGI_APPLICATION = 'online_store.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [BASE_DIR / 'static']

STATIC_ROOT = 'staticfiles'

# Путь к директории, где будут храниться загружаемые файлы
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL, по которому файлы будут доступны
MEDIA_URL = '/media/'

LOGIN_URL = '/login'

AUTH_USER_MODEL = 'myapp.CustomUser'

TOKEN_EXPIRE_SECONDS = 6000

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ("myapp.api.authentication.TokenExpireAuthentication",),
}


# Optional
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
# Required
AWS_STORAGE_BUCKET_NAME = 'python11deploy'
AWS_S3_REGION_NAME = 'us-east-1'  # e.g. us-east-2
AWS_ACCESS_KEY_ID = os.environ.get('AWS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET')
# НЕ ВПИСЫВАЙТЕ САМИ КЛЮЧИ, ТОЛЬКО os.environ.get('SOME_KEY')

# Tell the staticfiles app to use S3Boto3 storage when writing the collected static files (when
# you run `collectstatic`).
STORAGES = {
    "default": {
        "BACKEND": 'storages.backends.s3boto3.S3Boto3Storage',
    },
    "staticfiles": {
        "BACKEND": 'storages.backends.s3boto3.S3Boto3Storage',
    },
}

if os.environ.get('PROD'):
    try:
        from .settings_prod import *
    except ImportError:
        pass
else:
    try:
        from .settings_local import *
    except ImportError:
        pass

