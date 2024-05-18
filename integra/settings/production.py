import os
from .base import *

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY', 'qy5hre=w=a7gzw9x4w_f)v+-f6s!wjd002z4apb35-baoyr8rr^')

ALLOWED_HOSTS = ['localhost']

SECURE_HSTS_SECONDS = 3600
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
