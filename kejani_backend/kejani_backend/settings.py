from logging import config, debug
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*vo$neq=&0x(uz$p=8$!=f-vk(2k!!cv&dm-%k(q&mt0ij)ci)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)


ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "0.0.0.0"
]


# Application definition

LOGGING = {
    "version":1,
    "disable_existing_loggers":False,
    "handlers":{
        "file":{
            "level":"DEBUG",
            "class":"logging.FileHandler",
            "filename":"debug.log",
        },
    },
    "loggers":{
        "django":{
            "handlers":["file"],
            "level":"DEBUG",
            "propagate":True,
        },
    },
}



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'kejani_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kejani_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "NAME":config("DB_NAME",defaualt="kejani_db"),
        "USER":config("DB_USER", default="kejani_user"),
        "PASSWORD":config("DB_HOST", default="localhost"),
        "HOST":config("DB_PORT", default="localhost"),
        "PORT":config("DB_PORT", default="54232"),    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

#where colleststatic will put files (for production)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]



# Media files (user uploads)
MEDIA_URL = '/media/'
MEDIA_URL = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'






SPECTACULAR_SETTINGS = {
    'TITLE': 'Ke-jani API',
    'DESCRIPTION': '''
    *Ke-jani Backend API Documentation*

    Welcome to the Ke-jani API - a platform that connects generosity with need.

    ''',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'CONTACT': {
        'name': 'ke-jani Support',
        'email': 'info@ke-jani.co.ke',
        'url': '',
    },
    'LICENSE': {
        'name': 'Proprietary',
        'url': 'https://ke-jani.co.ke/terms',
    },
    'EXTERNAL_DOCS': {
        'description': 'Ke-jani Documentation',
        'url': 'https://ke-jani.co.ke/api/docs',
    },
    
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'JWT authorization header using the Bearer scheme. Example: "Authorization: Bearer {token}"'
        }
    },
    'SECURITY': [{'Bearer': []}],
    
    # NEW: Additional Swagger UI settings for better JWT experience
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'persistAuthorization': True,
        'displayOperationId': False,
        'defaultModelsExpandDepth': 1,
        'defaultModelExpandDepth': 1,
        'defaultModelRendering': 'example',
        'displayRequestDuration': True,
        'docExpansion': 'none',
        'filter': True,
        'operationsSorter': 'alpha',
        'showExtensions': True,
        'showCommonExtensions': True,
        'tagsSorter': 'alpha',
        'tryItOutEnabled': True,
        'validatorUrl': None,
    },
    
    # NEW: Server configuration
    'SERVERS': [
        {'url': 'http://127.0.0.1:8000', 'description': 'Development server'},
        {'url': 'https://ke-jani.co.ke', 'description': 'Production server'},
    ],
}



CORS_ALLOWED_ORIGINS=[
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

