from _base import *

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('TEST_DATABASE_NAME'),
        'USER': os.getenv('TEST_DATABASE_USER'),
        'PASSWORD': os.getenv('TEST_DATABASE_PASSWORD'),
        'HOST': os.getenv('TEST_DATABASE_HOST'),
        'PORT': os.getenv('TEST_DATABASE_PORT'),
    }
}
