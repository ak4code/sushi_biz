from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(env_file=str(BASE_DIR / '.env'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default=False)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'solo.apps.SoloAppConfig',
    'tinymce.apps.TinymceConfig',
    'adminsortable',
    'webpack_loader',
    'genericadmin',
    'import_export',
    'rest_framework',
    'django_filters',
    'easy_thumbnails',
    'maintenancemode',
    # my_apps
    'home.apps.HomeConfig',
    'shop.apps.ShopConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'maintenancemode.middleware.MaintenanceModeMiddleware',
]

ROOT_URLCONF = 'sushi_biz.urls'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
    'default': env.db('DATABASE_URL', default='sqlite:///db.sqlite3')
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'home.context_processors.menu',
            ],
        },
    },
]

WSGI_APPLICATION = 'sushi_biz.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators


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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATETIME_FORMAT = "d.m.Y H:M"
DATE_FORMAT = "d.m.Y"
SHORT_DATE_FORMAT = "d.m.Y"

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

TINYMCE_DEFAULT_CONFIG = {
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': 'link image preview codesample contextmenu table code lists textcolor colorpicker paste media',
    'toolbar1': 'formatselect | fontselect | forecolor | backcolor | bold italic underline | alignleft aligncenter alignright alignjustify '
                '| bullist numlist | outdent indent | table | link image | codesample | preview code | media',
    'contextmenu': 'formats | link image',
    'menubar': False,
    'media_live_embeds': True,
    'paste_as_text': True,
    'valid_elements': '*[*]',
    'inline': False,
    'statusbar': True,
    'width': 'auto',
    'height': 360,
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 30,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

THUMBNAIL_ALIASES = {
    '': {
        'small_crop': {'size': (200, 200), 'quality': 80, 'crop': True},
        'small': {'size': (200, 200), 'quality': 80, 'crop': False},
        'medium_crop': {'size': (350, 350), 'quality': 80, 'crop': True},
        'medium': {'size': (350, 350), 'quality': 80, 'crop': False},
    },
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        'TIMEOUT': 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

TG_BOT_TOKEN = env('TG_BOT_TOKEN')
TG_GROUP = env('TG_GROUP_ID')

MAINTENANCE_MODE = False
MAINTENANCE_ALLOW_STAFF = True
MAINTENANCE_ALLOW_SUPERUSER = True
MAINTENANCE_IGNORE_URLS = (
    r'^/admin',
)