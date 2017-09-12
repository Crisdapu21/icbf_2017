import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'md+=+p9&m*34v_)7w9fm&6h4=40h#(g09t552u3yeyu46w^imq'
DEBUG = False

URL = "https://s3.amazonaws.com/icbf-2017/"
SERVIDOR = "https://controlydesarrollo.herokuapp.com"
AWS_STORAGE_BUCKET_NAME = 'icbf-2017'
AWS_ACCESS_KEY_ID = 'AKIAJMWYEBDRPUXIB5UA'
AWS_SECRET_ACCESS_KEY = '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'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_URL = 'https://s3.amazonaws.com/icbf-2017/'
ALLOWED_HOSTS = ["*"]

if not DEBUG:
    ALLOWED_HOSTS = ["*"]
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SEaCURE_HSTS_INCLUDE_SUBDOMAINS = True
    USE_X_FORWARDED_HOST = True


INSTALLED_APPS = [
    'admin_interface',
    'flat_responsive',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'parametrizacion',
    'login',
    'operarios',
    'entidad_administradora_servicio',
    'beneficiarios',
    'caracteristicas_vivienda',
    'composicion_familiar',
    'relaciones_comunitarias',
    'calendario',
    'nutricion',
    'salud',
    'storages',
    'djcelery',
    'kombu.transport.django',
]


MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'icbf.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+'/templates'],
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

from django.contrib.messages import constants as message_constants
MESSAGE_LEVEL = message_constants.DEBUG
WSGI_APPLICATION = 'icbf.wsgi.application'

"""
DATABASES = {
        'default': {
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.sqlite3',
    }
}
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dvnj0mh3eokne',
        'USER': 'tajibkgilmttmj',
        'PASSWORD': '93d9ffd41ae417265532fae74a8c4875c627f3aac1b9dac4f8d58d8bcb2101a6',
        'HOST': 'ec2-54-235-80-137.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

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

GRUPO1 = "ADMINISTRADORES"
GRUPO2 = "OPERARIOS"

LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_L10N = True
USE_TZ = True
