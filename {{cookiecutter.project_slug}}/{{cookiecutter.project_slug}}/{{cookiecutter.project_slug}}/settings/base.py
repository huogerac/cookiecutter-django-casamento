# -*- coding: utf-8 -*-
"""
Django settings for djenietemplate project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from os import environ, pardir
from os.path import abspath, basename, dirname, join, normpath
from sys import path
from datetime import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# Absolute filesystem path to the Django project directory:
BASE_DIR = dirname(dirname(__file__))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(BASE_DIR)

SITE_NAME = basename(BASE_DIR)


# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(BASE_DIR)

ADMINS = (
    ('{{cookiecutter.author_name}}', '{{cookiecutter.email}}'),
)

MANAGERS = ADMINS


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = r"g*w1mrha3x&q8a7*748#4+j0ne6s=il%y=74m$e270fo!76c=z"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

ROOT_URLCONF = '%s.urls' % SITE_NAME

WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

SITE_ID = environ.get('DJANGO_SITE_ID', 1)

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))
MEDIA_URL = '/media/'

STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

# django-bower
BOWER_COMPONENTS_ROOT = normpath(join(SITE_ROOT, 'components'))

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)


FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'core.context_processors.configuracoes_processor',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
    normpath(join(SITE_ROOT, 'themes', 'templates')),       # django-floppyforms
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    #'django.contrib.sites',
    #'django.contrib.sitemaps',       # App to generate the sitemaps
)

THIRD_PARTY_APPS = (
    'south',                          # Database migration helpers
    'djangobower',                    # django-bower
    'floppyforms',                    # django-floppyforms
    'django_extensions',              # django-extensions
    'ckeditor',                       # django-ckeditor-updated
    'djrill',                         # djrill email integration
)

LOCAL_APPS = (
    'core',
    'themes',
    'fotos',
    'rsvp',
    'listapresentes',
    'fornecedores',
    'roteiros',
)

BOWER_INSTALLED_APPS = (
    'bootstrap#3.2.0',
    'jquery#1.11.3',
    'font-awesome-bower#4.2.0',
    'classie#1.0.1',
    'modernizr#~2.8.3',
    'animate.css#3.2.0',
    'waypoints#3.0.1',
    )

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# django-ckeditor-updated
CKEDITOR_UPLOAD_PATH = normpath(join(MEDIA_ROOT, 'uploads'))
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'height': 340,
        'width': 680,
    },
}

LOGIN_URL = '/auth/'

# Enquanto nada esta certo ainda, apenas a data, mantenha este como True,
# senão False para exibir normalmente todas as páginas
DJ_CASAMENTO_MODO_SAVE_THE_DATE = False

# Nome dos noivos
DJ_CASAMENTO_DE_UM_LADO = '{{cookiecutter.casamento_de}}'
DJ_CASAMENTO_DO_OUTRO = '{{cookiecutter.com}}'

# Dia e local
DJ_CASAMENTO_DATA = '{{cookiecutter.data_hora}}:00'.replace('-', '/')
DJ_CASAMENTO_LOCAL = u'{{cookiecutter.local}}'
DJ_CASAMENTO_CIDADE = u'{{cookiecutter.cidade}}'
DJ_CASAMENTO_DATE = datetime.strptime(DJ_CASAMENTO_DATA, '%Y/%m/%d %H:%M:%S')

# Outros
DJ_CASAMENTO_JA_ACONTECEU = datetime.today() >= DJ_CASAMENTO_DATE
DJ_CASAMENTO_EMAIL_CONTATO = '{{cookiecutter.email_contato}}'
DJ_CASAMENTO_FONE_CONTATO = '{{cookiecutter.fone_contato}}'
DJ_CASAMENTO_SERVER = '{{cookiecutter.dominio}}'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
