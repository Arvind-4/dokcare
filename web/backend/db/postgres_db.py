import pathlib

from backend.env import config

DATABASE_NAME = config("DATABASE_NAME", cast=str)
DATABASE_USER = config("DATABASE_USER", cast=str)
DATABASE_PASSWORD = config("DATABASE_PASSWORD", cast=str)
DATABASE_HOST = config("DATABASE_HOST", cast=str)
DATABASE_PORT = config("DATABASE_PORT", cast=int)

CERTIFICATE_DIR = BASE_DIR = (
    pathlib.Path(__file__).resolve().parent.parent.parent.parent
)

CERTIFICATE_FILE_PATH = CERTIFICATE_DIR / "certificate" / "root.crt"

DB_IS_AVAILABLE = all(
    [
        DATABASE_NAME,
        DATABASE_USER,
        DATABASE_PASSWORD,
        DATABASE_HOST,
        DATABASE_PORT,
        CERTIFICATE_FILE_PATH,
    ]
)

if DB_IS_AVAILABLE:
    DATABASES = {
        "default": {
            "ENGINE": "django_cockroachdb",
            "NAME": DATABASE_NAME,
            "USER": DATABASE_USER,
            "PASSWORD": DATABASE_PASSWORD,
            "HOST": DATABASE_HOST,
            "PORT": DATABASE_PORT,
            "OPTIONS": {
                "sslmode": "verify-full",
                "sslrootcert": str(CERTIFICATE_FILE_PATH),
            },
        },
    }

print("DB is ready: ", DB_IS_AVAILABLE)
