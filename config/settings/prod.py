from .base import *

DEBUG = True  # 실제 배포 시에는 False로
ALLOWED_HOSTS = ['*']  # 추후 배포할 호스트 주소 입력 예정
INSTALLED_APPS += []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
        'OPTIONS': {
            'unix_socket': None,
        }
    }
}

print(os.getenv('DATABASE_NAME'))
print(os.getenv('DATABASE_USER'))
print(os.getenv('DATABASE_PASSWORD'))
print(os.getenv('DATABASE_NAME'))
print(os.getenv('DATABASE_HOST'))
print(os.getenv('DATABASE_PORT'))
