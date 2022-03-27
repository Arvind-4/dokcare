from .base import *

import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY', 'secret')

ADMIN_URL = os.environ.get('ADMIN_URL', '/admin/')

MY_URL = os.environ.get('MY_URL')

ALLOWED_HOSTS.append(MY_URL)

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
