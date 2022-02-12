from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [".williamisamazing.tk", "williamisamazing.tk"]

ADMINS = [
    (
        "William Ferreira",
        "williammmferreira16@gmail.com"
    )
]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'chat_db',
		'USER': 'chat_db_user',
		'PASSWORD': os.getenv("POSTGRES_PASSWORD"),
        'HOST': 'localhost',
        'PORT' : 5432,
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Set to true when serving the site over https, and only https
SECURE_HSTS_SECONDS = False