from _base import *

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'

load_dotenv(dotenv_path=env_path)

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