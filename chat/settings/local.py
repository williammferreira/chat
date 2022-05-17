from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost',
                 'williamisamazing.com', ".williamisamazing.com"]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'chat_db',
                'USER': 'chat_db_user',
                'PASSWORD': os.getenv("POSTGRES_PASSWORD"),
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
