import os
import pathlib
from dotenv import load_dotenv

from .base import *

if not "HEROKU" in os.environ:
    load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = str(os.environ.get('DJANGO_SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DJANGO_DEBUG')))

ADMIN_URL = str(os.environ.get('DJANGO_ADMIN_URL'))

ALLOWED_HOSTS = []
ALLOWED_HOSTS.extend(
    filter(
        None,
        str(os.environ.get('DJANGO_ALLOWED_HOSTS', '')).split(','),
    )
)

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'static-root'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASE_NAME = str(os.environ.get('DATABASE_NAME'))
DATABASE_USER = str(os.environ.get('DATABASE_USER'))
DATABASE_PASSWORD = str(os.environ.get('DATABASE_PASSWORD'))
DATABASE_HOST = str(os.environ.get('DATABASE_HOST'))
DATABASE_PORT = int(os.environ.get('DATABASE_PORT', 0))

CERTIFICATE_DIR = BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent.parent

CERTIFICATE_FILE_PATH = CERTIFICATE_DIR / 'certificate' / 'root.crt'

DB_IS_AVAILABLE = all([
    DATABASE_NAME,
    DATABASE_USER,
    DATABASE_PASSWORD,
    DATABASE_HOST,
    DATABASE_PORT,
    CERTIFICATE_FILE_PATH,
])

if DB_IS_AVAILABLE:
    print('Production ', DB_IS_AVAILABLE)
    DATABASES = {
        'default': {
            'ENGINE': 'django_cockroachdb',
            'NAME': DATABASE_NAME,
            'USER': DATABASE_USER,
            'PASSWORD': DATABASE_PASSWORD,
            'HOST': DATABASE_HOST,
            'PORT': DATABASE_PORT,
            'OPTIONS': {
                'sslmode': 'verify-full',
                'sslrootcert': str(CERTIFICATE_FILE_PATH),
            },
        },
    }

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = str(os.environ.get('EMAIL_HOST_USER'))
EMAIL_HOST_PASSWORD = str(os.environ.get('EMAIL_HOST_PASSWORD'))