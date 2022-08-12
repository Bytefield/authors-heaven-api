from .base import *
from .base import env

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="9Qw51BW2g1YyfZ2"
)

# django-insecure-v!qax+df1qb-872yg*81^417e36cxb*h!0)he9-*p)14codslt

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]