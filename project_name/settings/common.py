"""
Django settings for Project

"""

import sys
from os import getenv
from os.path import join, normpath, basename
from pathlib import Path
from dotenv import load_dotenv


# =========PATH CONFIGURATION =======================

# Django Project Settings Directory
DJANGO_ROOT = Path(__file__).resolve().parent.parent

# Project Root Folder
PROJECT_ROOT = DJANGO_ROOT.parent

# the name of the whole site
SITE_NAME = basename(DJANGO_ROOT)

# Project Templates
TEMPLATES_ROOT = [join(PROJECT_ROOT, 'templates'), ]

# Static Files
STATIC_ROOT = join(PROJECT_ROOT, 'run', 'static')

# Media Files
MEDIA_ROOT = join(PROJECT_ROOT, 'run', 'media')

# Local Statics
STATICFILES_DIRS = [join(PROJECT_ROOT, 'static')]


# add apps/ to the Python path
sys.path.append(normpath(join(PROJECT_ROOT, 'apps')))

# Environment Variables path
load_dotenv(join(PROJECT_ROOT, 'configs', '.env'))


# ==================== APPLICATION CONFIG =========================

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = ['crispy_forms', ]

LOCAL_APPS = ['accounts', ]

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

AUTH_USER_MODEL = 'accounts.CustomUser'

# Template Pack for crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATES_ROOT,
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


# Password validation
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

# ================== DJANGO RUNNING CONFIGURATION =================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# the default WSGI application
WSGI_APPLICATION = f'{SITE_NAME}.wsgi.application'

# the root URL configuration
ROOT_URLCONF = f'{SITE_NAME}.urls'

# SECRET_KEY
SECRET_KEY = str(getenv("SECRET_KEY"))

DEBUG = str(getenv("DEBUG")) == 'True'


# url for static files
STATIC_URL = '/static/'

# url for media files
MEDIA_URL = '/media/'

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
