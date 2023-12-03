from .base import *  # noqa
from .base import env

ADMINS = [("Jason Hall", "jason.kei.hall@gmail.com")]

# TODO add domain names of the production server
CSRF_TRUSTED_ORIGINS = [""]

SECRET_KEY = env('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=[''])

ADMIN_URL = env.('DJANGO_ADMIN_URL')

DATABASES = {'default': env.db('DATABASE_URL')}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_SSL_REDIRECT = env.bool('DJANGO_SECURE_SSL_REDIRECT', default=True)

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

# TODO: change to 518400 later
SECURE_HSTS_SECONDS = 60

SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool('DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True)

SECURE_CONTENT_TYPE_NOSNIFF = env.bool('DJANGO_SECURE_CONTENT_TYPE_NOSNIFF',default=True)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL', default='jason.kei.hall@gmail.com')

SITE_NAME = 'Medium API Clone'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

