from backend.env import config

from .base import *

SECRET_KEY = config('DJANGO_SECRET_KEY', cast=str)

DJANGO_DEBUG = config('DJANGO_DEBUG', cast=bool, default=False)
DEBUG = DJANGO_DEBUG

DJANGO_LIVE = config('DJANGO_LIVE', cast=bool)

ADMIN_URL = config('DJANGO_ADMIN_URL', cast=str)

ALLOWED_HOSTS = []
ALLOWED_HOSTS.extend(
    filter(
        None,
        config('DJANGO_ALLOWED_HOSTS', cast=str).split(','),
    )
)

APPEND_SLASH = True

INSTALLED_APPS = DJANGO_DEFAULT_APPS + THIRD_PARTY_APPS + USER_DEFINED_APPS

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware') 

WSGI_APPLICATION = 'backend.wsgi.application'
ASGI_APPLICATION = 'backend.asgi.application'

STATICFILES_DIRS = [BASE_DIR / 'static',]
STATIC_ROOT = BASE_DIR.parent / 'staticfiles_build' / 'static'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.parent / 'media'


from backend.db.postgres_db import * #noqa
from backend.email.gmail import * #noqa

if DJANGO_LIVE and not DJANGO_DEBUG:
    print("SECURE SETTINGS")
    SECURE_HSTS_SECONDS = True 
    SECURE_HSTS_PRELOAD = True

    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

print("DJANGO_LIVE:", DJANGO_LIVE)
print("DJANGO_DEBUG:", DJANGO_DEBUG)