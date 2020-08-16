DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ralph',
        'USER': 'ralph',
        'PASSWORD': 'r091016r',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = False

ALLOWED_HOSTS = ['142.93.169.187', 'ralphsubrio.me']

SECRET_KEY = 'ta_rhwlxoka)s!yy5)-%bijif9!5(gkr#o9)$vsaxd2+v0-6yd'

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
)