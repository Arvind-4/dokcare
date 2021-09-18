from .base import *

import os
from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')

ADMIN_URL = os.environ.get('ADMIN_URL')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
