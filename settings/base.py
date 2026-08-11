import sys
import os
from pathlib import Path

import decouple


BASE_DIR = Path(__file__).resolve().parent.parent
APPS_DIR = os.path.join(BASE_DIR, 'apps') 
sys.path.append(BASE_DIR)
sys.path.append(APPS_DIR)

SECRET_KEY = decouple.config('SECRET_KEY', cast=str)

DEBUG = decouple.config('DEBUG', True, cast=bool)

HOST = decouple('HOST', '127.0.0.1', cast=str)
DOMAIN = 'https://' + HOST

ALLOWED_HOSTS = (
    'localhost',
    '127.0.0.1',
    HOST,
)

CSRF_TRUSTED_ORIGINS = (
    'http://127.0.0.1:8080',
    DOMAIN,
)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

CUSTOM_APPS = (
    'products',
)

INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'settings.urls'

TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (
            'templates/',
        ),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ),
        },
    },
)

WSGI_APPLICATION = 'settings.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': decouple.config('DB_NAME', cast=str),
        'USER': decouple.config('DB_USER', cast=str),
        'PASSWORD': decouple.config('DB_PASS', cast=str),
        'HOST': decouple.config('DB_HOST', 'localhost', cast=str),
        'PORT': decouple.config('DB_PORT', '5432', cast=int),
    }
}

AUTH_PASSWORD_VALIDATORS = (
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa: E501
    },
)

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}

# Stript API keys
STRIPE_SEC_KEY = decouple.config('STRIPE_SEC_KEY', cast=str)
STRIPE_PUB_KEY = decouple.config('STRIPE_PUB_KEY', cast=str)

CURRENCIES = (
    (1, 'usd'),
    (2, 'eur'),
)
