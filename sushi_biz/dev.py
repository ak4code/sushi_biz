from .settings import *

ALLOWED_HOSTS = ['*']

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': '/',
        'STATS_FILE': BASE_DIR / 'webpack-stats.json',
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map', r'.+\node_modules'],
    }
}

INTERNAL_IPS = ['127.0.0.1', ]

X_FRAME_OPTIONS = 'SAMEORIGIN'