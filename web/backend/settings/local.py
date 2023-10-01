from backend.env import config

from .base import *

SECRET_KEY = "ny9nwybew$fq1gf)+c4#oj@b2wtqms*rb&5@(u8*gdir$x3hp&"

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = DJANGO_DEFAULT_APPS + THIRD_PARTY_APPS + USER_DEFINED_APPS

MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

WSGI_APPLICATION = "backend.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


ADMIN_URL = config("DJANGO_ADMIN_URL", cast=str, default="admin/")

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR.parent / "staticfiles"

MEDIA_URL = "/media/"
MEDIAFILES_DIR = [
    BASE_DIR / "media",
]
MEDIA_ROOT = BASE_DIR / "media"

INTERNAL_IPS = (
    "127.0.0.1",
    "192.168.1.23",
    "localhost:3000",
)

APPEND_SLASH = True

from backend.email.gmail import *  # noqa
