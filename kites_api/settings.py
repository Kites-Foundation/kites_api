from pathlib import Path

import environ
import sentry_sdk
from healthy_django.healthcheck.django_database import DjangoDatabaseHealthCheck
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

environ.Env.read_env()
SECRET_KEY = env("SECRET", default="django-insecure-jow#rf4lx#f6-el@i_0o2m(gfcz%0-r6i=8@p1-vtit508olua")

DEBUG = env("DEBUG", default=True)
ALLOWED_HOSTS = ["*"]

# Application definition

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
                    'rest_framework.authtoken', 'rest_framework_simplejwt']

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + CUSTOM_APPS

CSRF_TRUSTED_ORIGINS = ['https://*.kitesfoundation.org']

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

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'postgres': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kites-4',
        'USER': 'postgres',
        'PASSWORD': 'tomahawk@T1',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
WHITENOISE_MANIFEST_STRICT = True

EMAIL_BACKEND = 'django_ses.SESBackend'

AWS_SES_ACCESS_KEY_ID = 'YOUR-ACCESS-KEY-ID'
AWS_SES_SECRET_ACCESS_KEY = 'YOUR-SECRET-ACCESS-KEY'
AWS_SES_REGION_NAME = 'ap-south-1'
AWS_SES_REGION_ENDPOINT = 'email-smtp.ap-south-1.amazonaws.com'
AWS_SES_CONFIGURATION_SET = 'kites'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = "sgbackend.SendGridBackend"
# # SENDGRID_API_KEY = env('SENDGRID_API_KEY')
#
# SENDGRID_API_KEY = env('SENDGRID_API_KEY',
#                        default="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")
# if not SENDGRID_API_KEY:
#     raise RuntimeError("SENDGRID API KEY is not set!")

# CORS fix
CORS_ORIGIN_ALLOW_ALL = True
SENTRY_DSN = env("SENTRY_DSN", default="")

default_configuration = [
    DjangoDatabaseHealthCheck("Database", slug="rds-kites", connection_name="default"),
]
HEALTHY_DJANGO = default_configuration
sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[DjangoIntegration()],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=0.0,
    auto_session_tracking=True,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
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
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

AUTH_USER_MODEL = 'users.User'

SIMPLE_JWT = {
    'UPDATE_LAST_LOGIN': True,
    'ALGORITHM': 'HS512'
}
