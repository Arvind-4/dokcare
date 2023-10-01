import os
import sys
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent

PATHS = [
    str(BASE_DIR / "web"),
    str(BASE_DIR / "web" / "backend"),
]

sys.path.extend(PATHS)

os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

import django
django.setup()

from web.backend.asgi import get_asgi_application
app = get_asgi_application()