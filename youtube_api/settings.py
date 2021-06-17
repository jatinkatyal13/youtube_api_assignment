import os
from pathlib import Path

from youtube_api.config import Config


BASE_DIR = Path(__file__).resolve().parent.parent

os.environ.setdefault("PYTHONPATH", str(BASE_DIR))

SECRET_KEY = Config.SECRET_KEY

DEBUG = Config.DEBUG

ALLOWED_HOSTS = Config.ALLOWED_HOSTS

INSTALLED_APPS = [
    "api",
    "rest_framework",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ]
}

ROOT_URLCONF = "youtube_api.urls"

WSGI_APPLICATION = "youtube_api.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": Config.DB_NAME,
        "USER": Config.DB_USER,
        "PASSWORD": Config.DB_PASSWORD,
        "HOST": Config.DB_HOST,
    }
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
