from .base import *


DEBUG = True
ALLOWED_HOSTS = ['*']  # 모든 호스트 허용
INSTALLED_APPS += []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}