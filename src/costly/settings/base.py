"""
Django settings for costly project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import os
from django.urls import reverse_lazy
from pathlib import Path

DEBUG = True

"""
    Note for running in dev and on IIS
    for dev, this alias (url prefix) is blank
    for IIS - use production.py settings, which loads base, then production where this is set to IIS's name
    for the app
    
"""

IIS_APP_ALIAS = r'costly/'
IIS_APP_ALIAS = ''



# Build paths inside the project like this: BASE_DIR / "directory"
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

# this is for static files not found in an app
# costly is not an included app, so it needs to be specified directly
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'costly', 'static'),
    # os.path.join(BASE_DIR, 'scenario', 'static'), # this is automatically included
]

# this is where collectstatic will put all the documents it collects
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


MEDIA_URL = '/' + IIS_APP_ALIAS + 'media/'

STATIC_URL = '/' + IIS_APP_ALIAS + 'static/'



# Use Django templates using the new Django 1.8 TEMPLATES settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'costly', 'templates'),
            os.path.join(BASE_DIR, 'scenario','templates'),
            # insert more TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [
                'scenario.templatetags.scenario_extras',
            ]
        },
    },
]

# Use 12factor inspired environment variables or from a file
import environ
env = environ.Env()

# Create a local.env file in the settings directory
# But ideally this env file should be outside the git repo
env_file = Path(__file__).resolve().parent / 'local.env'
if env_file.exists():
    environ.Env.read_env(str(env_file))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.humanize',
    'bootstrap4',
    'bootstrap_datepicker_plus',

    'rest_framework',
    'rest_framework_datatables',

    'mathfilters',

    'django_tables2',
    # 'authtools',
    'crispy_forms',
    'easy_thumbnails',
    'django_select2',
    'multiselectfield',
    'intl_tel_input',
    'widget_tweaks',
    'djmoney',
    # 'django_filters',
    'location_field.apps.DefaultConfig',
    'authtools',
    'profiles',
    'accounts',
    'testapp',
    'scenario.apps.ScenarioConfig',

)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'costly.urls'

WSGI_APPLICATION = 'costly.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

# DATABASES = {
#     # Raises ImproperlyConfigured exception if DATABASE_URL not in
#     # os.environ
#     'default': env.db(),
# }

#TODO 2019-05-31 at 15:11
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'costtool',
		'USER': 'postgres',
		'PASSWORD': 'friedCatRacket21',
		'HOST': '127.0.0.1',
		'PORT': '5433',
		'DATABASE_SCHEMA': 'pubic'
	}
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True
USE_TZ = True


# Crispy Form Theme - Bootstrap 3
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# For Bootstrap 3, change error alert to 'danger'
from django.contrib import messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Authentication Settings
AUTH_USER_MODEL = 'authtools.User'

LOGIN_REDIRECT_URL = reverse_lazy("scenario:index")

LOGIN_URL = reverse_lazy("accounts:login")

THUMBNAIL_EXTENSION = 'png'     # Or any extn for your thumbnails

# Use BOOTSTRAP3 if you are using Bootstrap 3
# BOOTSTRAP4 = {
#     'include_jquery': True,
#
# }

# DRF
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_datatables.renderers.DatatablesRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_datatables.filters.DatatablesFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework_datatables.pagination.DatatablesPageNumberPagination',
    'PAGE_SIZE': 50,
}

DJANGO_TABLES2_TEMPLATE = {
    "DJANGO_TABLES2_TEMPLATE": "django_tables2/table.html",
}

# https://github.com/django-money/django-money
CURRENCIES = ('USD',)
CURRENCY_CHOICES = [('USD', 'USD $'), ]