from pathlib import Path

import os
import environ
import sentry_sdk
import dotenv
from healthy_django.healthcheck.django_database import DjangoDatabaseHealthCheck
from sentry_sdk.integrations.django import DjangoIntegration

BASE_DIR = Path(__file__).resolve().parent.parent

if Path(".env").is_file():
    dotenv.read_dotenv(str(BASE_DIR / ".env"))

SECRET_KEY = os.environ.get("SECRET", default="django-insecure-jow#rf4lx#f6-el@i_0o2m(gfcz%0-r6i=8@p1-vtit508olua")

DEBUG = os.environ.get("DEBUG", default=True)
ALLOWED_HOSTS = ["*"]
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = os.environ.get("AWS_S3_CUSTOM_DOMAIN")
CLOUDFRONT_DOMAIN = os.environ.get("CLOUDFRONT_DOMAIN", None)
CLOUDFRONT_ID = os.environ.get("CLOUDFRONT_ID", None)
AWS_CLOUDFRONT_KEY = os.environ.get("AWS_CLOUDFRONT_KEY", None).encode('ascii')
AWS_CLOUDFRONT_KEY_ID = os.environ.get("AWS_CLOUDFRONT_KEY_ID", None)
AWS_SES_ACCESS_KEY_ID = os.environ.get('YOUR-ACCESS-KEY-ID', None)
AWS_SES_SECRET_ACCESS_KEY = os.environ.get('YOUR-SECRET-ACCESS-KEY', None)
SENTRY_DSN = os.environ.get("SENTRY_DSN", default="")

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

CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS', ['https://*.kitesfoundation.org', 'https://*.kites.foundation'])

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
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_NAME", 'kites-4'),
        'USER': os.environ.get("DB_USER", 'postgres'),
        'PASSWORD': os.environ.get("DB_PASSWORD", 'tomahawk@T1'),
        'HOST': os.environ.get("DB_HOST", '127.0.0.1'),
        'PORT': os.environ.get("DB_PORT", '5432'),
    }
}




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

DEFAULT_FROM_EMAIL = os.environ.get(
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
