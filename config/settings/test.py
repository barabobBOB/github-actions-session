from .base_settings import *

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('TEST_DATABASE_NAME'),
        'USER': env('TEST_DATABASE_USER'),
        'PASSWORD': env('TEST_DATABASE_PASSWORD'),
        'HOST': env('TEST_DATABASE_HOST'),
        'PORT': env('TEST_DATABASE_PORT'),
    }
}