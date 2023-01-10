import os
from pathlib import Path

from django.urls import reverse, reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-6$gkou2mikz*)r_1i9s1t@boav)_e+5qeo06j$i=+7a0=c1e+6'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'yourdomain.com', 'localhost']
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1', 'http://localhost:8000']
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8000',
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'store',
    'basket',
    'account',
    'payment',
    'orders',

    'django_extensions',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'settings.urls'

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
                'store.context_processors.categories',
                'basket.context_processors.basket',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'account.UserBase'
LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = reverse_lazy('account:dashboard')

PASSWORD_RESET_TIMEOUT_DAYS = 2

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# stripe payment
STRIPE_PUBLISHABLE_KEY = 'pk_test_51MONwDBlafiM1XPR4QImWUi1iYocnjdirTLwPcRG4JLRA4Ne21UmAdH1WxTnMHFU9CoikdBBDUX17wpt9crgMT2q00EqU5OVnh'
STRIPE_SECRET_KEY = 'sk_test_51MONwDBlafiM1XPR8xZ8kXCfqlHxkfrMrFNEbPB3455Eh1LsQDtCvzHkLmWuPZyrviihQtXdc293M0dAdMv9qyLl00fOYEcMkC'
# stripe listen --forward-to localhost:8000/payment/webhook/
STRIPE_ENDPOINT_SECRET = 'whsec_60b5b86108e85f9d10e1c4ac67089cf710a6babc774b1720f0ff34a0c2405bf7'