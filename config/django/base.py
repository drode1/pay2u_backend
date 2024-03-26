import os
from pathlib import Path

from faker import Faker

from config.env import APPS_DIR

SECRET_KEY: str = os.environ.get('SECRET_KEY', 'test-key')

DEBUG: bool = os.environ.get('DEBUG', False)
ALLOWED_HOSTS: list = os.environ.get('ALLOWED_HOSTS', '*').split(',')
CSRF_TRUSTED_ORIGINS: list = os.environ.get('CSRF_TRUSTED_ORIGINS', 'http://localhost').split(',')  # noqa: E501

LOCAL_APPS = [
    'app.core.apps.CoreConfig',
    'app.users.apps.UsersConfig',
    'app.auth_jwt.apps.AuthConfig',
    'app.subscriptions.apps.SubscriptionsConfig',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'django_json_widget',
    'corsheaders',
    'phonenumber_field',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(Path(APPS_DIR) / 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # noqa: E501
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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = Path(APPS_DIR) / 'static'
STATICFILES_DIRS = []

MEDIA_URL = '/media/'
MEDIA_ROOT = Path(APPS_DIR) / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.User'
DEFAULT_MAX_LENGTH_FIELD = 255
MAX_NAME_LENGTH = 20
MAX_EMAIL_LENGTH = 40

from config.settings.logs import *  # noqa
from config.settings.cors import *  # noqa
from config.settings.rest_framework import *  # noqa
from config.settings.email import *  # noqa

Faker._DEFAULT_LOCALE = 'ru_RU'
