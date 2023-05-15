from pathlib import Path
from config.settings import BASE_DIR

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-ip%^w*smn3b_2dkg)p-dg+v-)7z#+!a(@5haixd1v+b*j87q6l'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}