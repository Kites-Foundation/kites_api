from pathlib import Path

import os
import environ
import sentry_sdk
from healthy_django.healthcheck.django_database import DjangoDatabaseHealthCheck
from sentry_sdk.integrations.django import DjangoIntegration
import dj_database_url
from typing import Any, Dict, Optional

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env()
SECRET_KEY = env("SECRET", default="django-insecure-jow#rf4lx#f6-el@i_0o2m(gfcz%0-r6i=8@p1-vtit508olua")

DEBUG = env("DEBUG", default=True)
ALLOWED_HOSTS = ["*"]
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME", "")
AWS_S3_CUSTOM_DOMAIN = env("AWS_S3_CUSTOM_DOMAIN", "")
CLOUDFRONT_DOMAIN = env("CLOUDFRONT_DOMAIN", None)
CLOUDFRONT_ID = env("CLOUDFRONT_ID", None)
AWS_CLOUDFRONT_KEY = env("AWS_CLOUDFRONT_KEY", None).encode('ascii')
AWS_CLOUDFRONT_KEY_ID = env("AWS_CLOUDFRONT_KEY_ID", None)
AWS_SES_ACCESS_KEY_ID = 'YOUR-ACCESS-KEY-ID'
AWS_SES_SECRET_ACCESS_KEY = 'YOUR-SECRET-ACCESS-KEY'
SENTRY_DSN = env("SENTRY_DSN", default="")

AWS_DEFAULT_ACL = "public-read"
AWS_S3_REGION_NAME = "ap-south-1"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

CUSTOM_APPS = [
    'users',
]

THIRD_PARTY_APPS = ['rest_framework', 'drf_yasg', 'healthy_django', 'allow_cidr', 'django_ses',
                    'rest_framework.authtoken', 'rest_framework_simplejwt', 'storages']

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + CUSTOM_APPS

CSRF_TRUSTED_ORIGINS = env('CSRF_TRUSTED_ORIGINS', ['https://*.kitesfoundation.org', 'https://*.kites.foundation'])

MIDDLEWARE = [
    'allow_cidr.middleware.AllowCIDRMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kites_api.urls'

ALLOWED_CIDR_NETS = [
    "10.0.0.0/19",
    "10.0.32.0/19",
    "10.0.64.0/19",
    "10.0.96.0/19",
    "10.0.128.0/19",
    "10.0.160.0/19"
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kites_api.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'postgres': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DB_NAME", 'kites-4'),
        'USER': env("DB_USER", 'postgres'),
        'PASSWORD': env("DB_PASSWORD", 'tomahawk@T1'),
        'HOST': env("DB_HOST", '127.0.0.1'),
        'PORT': env("DB_PORT", '5432'),
    }
}

# def get_db_settings(
#         env_db_url: str,
#         env_db_timeout: Optional[str] = None,
# ) -> Dict[str, Any]:
#     CONN_MAX_AGE = 0 if DEBUG else 600
#     DB_URL = os.environ.get(env_db_url)
#     if not DB_URL:
#         return {}
#
#     db_config = dj_database_url.parse(url=DB_URL, conn_max_age=CONN_MAX_AGE)
#
#     PG_STATEMENT_TIMEOUT = os.environ.get(env_db_timeout) if env_db_timeout else None
#     if PG_STATEMENT_TIMEOUT:
#         db_config["OPTIONS"] = {
#             "options": f"-c statement_timeout={PG_STATEMENT_TIMEOUT}"
#         }
#     return db_config
#
#
# DEFAULT_DB_CONFIG = get_db_settings(
#     env_db_url="DATABASE_URL", env_db_timeout="PG_STATEMENT_TIMEOUT"
# )
#
# DATABASES = {"default": DEFAULT_DB_CONFIG}
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
WHITENOISE_MANIFEST_STRICT = True

EMAIL_BACKEND = 'django_ses.SESBackend'

AWS_SES_REGION_NAME = 'ap-south-1'
AWS_SES_REGION_ENDPOINT = 'email-smtp.ap-south-1.amazonaws.com'
AWS_SES_CONFIGURATION_SET = 'kites'

DEFAULT_FROM_EMAIL = env(
    "EMAIL_FROM", default="Kites Foundation <info@kitesfoundation.org>"
)

CORS_ORIGIN_ALLOW_ALL = True

default_configuration = [
    DjangoDatabaseHealthCheck("Database", slug="rds-kites", connection_name="default"),
]
HEALTHY_DJANGO = default_configuration
sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[DjangoIntegration()],
    traces_sample_rate=0.0,
    auto_session_tracking=True,
    send_default_pii=False,
)

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # 'rest_framework.permissions.IsAuthenticated',
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 14,
    "SEARCH_PARAM": "search_text",
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    ]
}

AUTH_USER_MODEL = 'users.User'

SIMPLE_JWT = {
    'UPDATE_LAST_LOGIN': True,
    'ALGORITHM': 'HS512',
    "ROTATE_REFRESH_TOKENS": True,
}

ADMINS = [("""👪""", "hey@syam.dev")]
MANAGERS = ADMINS
