"""
Django settings for vpmoprj project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import datetime
import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NG_BUILD_DIR = os.path.join(BASE_DIR, "dist")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k3xrb+p%cw%7r@8$el#$7hd6_zqp93-(ue(acl^jx-okpzo643'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["*"]

# Setting for storing user uploads in S3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_DEFAULT_ACL = None

# AWS Keys
AWS_ACCESS_KEY_ID = os.environ["VPMO_AWS_ACCESS"]
AWS_SECRET_ACCESS_KEY = os.environ["VPMO_AWS_SECRET"]
AWS_STORAGE_BUCKET_NAME = "vpmo"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    #'werkzeug_debugger_runserver',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    # 'vpmoapp',
    'vpmoauth',
    'vpmotree',
    "vpmodoc",
    'guardian',
    'channels',
]

"""
MIGRATION_MODULES = {
    #"guardian": None # Skipping the migrations from guardian
    "vpmoauth": None,
    "vpmotree": None
}
"""

AUTHENTICATION_BACKENDS = (
    'vpmoauth.auth_backend.AuthBackend', # this is default from vpmo
    'django.contrib.auth.backends.ModelBackend', # The default
    'guardian.backends.ObjectPermissionBackend',
)


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # two new lines added as part of resolving PK issue
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vpmoprj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
# #Make sure your host IP is a string
# ALLOWED_HOSTS = [
#     'http://127.0.0.1:8000',
#     'http://localhost:4200/',
#     ]

# CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200'
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)


WSGI_APPLICATION = 'vpmoprj.wsgi.application'


# DEBUG_TOOLBAR_PANELS = (
#
#     'debug_toolbar_mongo.panel.MongoDebugPanel',
#
# )
#
# DEBUG_TOOLBAR_MONGO_STACKTRACES = False


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

if False and DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "djongo",
            "NAME": "test-example-24",
            "host": "localhost",
            "port": 27017
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'cluster2',# Changing from cluster0
            'HOST':
            'mongodb://vpmoadmin:.Y&?L.?V,Kf,@cluster0-shard-00-00-6qb6a.mongodb.net:27017,cluster0-shard-00-01-6qb6a.mongodb.net:27017,cluster0-shard-00-02-6qb6a.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true'
        }
    }


TEST_MONGO_DATABASE = {
    'db': 'test-example',
    'host': ['localhost'],
    'port': 27017
}

# INSTALLED_APPS += ["django_mongoengine"]
#
#
# SESSION_ENGINE = 'django_mongoengine.sessions'
# SESSION_SERIALIZER = 'django_mongoengine.sessions.BSONSerializer'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}


JWT_AUTH = {
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=3000),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=30),
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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [NG_BUILD_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# look in the app and find a model named Account
AUTH_USER_MODEL = 'vpmoauth.MyUser'

# Pointing to the routing protocols for django-channels
ASGI_APPLICATION = "vpmoprj.routing.application"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}