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

DEBUG = True

ALLOWED_HOSTS = []

DROPLET_PASSWORD = 'h7A2f6pedqpJVwR'

SECRET_KEY = 'ta_rhwlxoka)s!yy5)-%bijif9!5(gkr#o9)$vsaxd2+v0-6yd'

CORS_ORIGIN_ALLOW_ALL = True

LOGIN_REDIRECT_URL = '/console/dashboard'
LOGOUT_REDIRECT_URL = '/console/login'

EMAIL_HOST_USER = 'ralph.subrio@gmail.com'
EMAIL_HOST_PASSWORD = 'wmxqjxpbrlujfzee'

"""
after pulling restart this things
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo nginx -t && sudo systemctl restart nginx

superuser
username: ralph
password: r091016r
"""