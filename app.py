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

import django

django.setup()

from web.backend.wsgi import get_wsgi_application  # noqa

app = get_wsgi_application()
