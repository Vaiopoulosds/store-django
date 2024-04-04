from threading import local
from .common import *
from .common import *



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'HOST': 'mysql',
        'USER': 'root',
        'PASSWORD': 'mypswd'
    }
}

CELERY_BROKER_URL= 'redis://redis:6379/1'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/2",
        "TIMEOUT": 10*60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

EMAIL_HOST='smtp4dev'
EMAIL_HOST_USER=''
EMAIL_HOST_PASSWORD=''
EMAIL_PORT= 2525


DEBUG_TOOLBAR_CONFIG={
  'SHOW_TOOLBAR_CALLBACK': lambda request:True
}
