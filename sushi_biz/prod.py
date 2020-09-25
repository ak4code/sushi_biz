from .settings import *

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': env.db('DATABASE_URL')
}

STATIC_ROOT = BASE_DIR / 'static'

ALLOWED_HOSTS = []

if not DEBUG:
    WEBPACK_LOADER.update({
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': BASE_DIR / 'webpack-stats-prod.json'
    })
