from .base import *

DEBUG = True  # 실제 배포 시에는 False로
ALLOWED_HOSTS = ['*']  # 추후 배포할 호스트 주소 입력 예정
INSTALLED_APPS += []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('test'),
        'USER': os.getenv('seyeon'),
        'PASSWORD': os.getenv('qwer1234'),
        'HOST': os.getenv('database-1.cjwccm2cmi84.ap-northeast-2.rds.amazonaws.com'),
        'PORT': os.getenv('3306'),
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
