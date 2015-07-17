from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kb',
        'USER': 'wikiTwUser',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

SOCIAL_AUTH_TWITTER_KEY = 'S4AjM2lAvQSRT5hZLXq0c4sa0'
SOCIAL_AUTH_TWITTER_SECRET = 'wI9zdg7sSA2hBivTN0WDr0ArQ5ZoxwgxQERgaFz3pIbyDHGLtq'
