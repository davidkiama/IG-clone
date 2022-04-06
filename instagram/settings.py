from pathlib import Path
import os

import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^ijs-2^ny$8%3$e!a4j**20%t*6xcnnbqqr=2stfeu492skg_8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.localhost', '.127.0.0.1', '.0.0.0.0',
                 '.django-instagram-clone-xxiv.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    "whitenoise.runserver_nostatic",
    "django.contrib.messages",
    "cloudinary",
    'django.contrib.staticfiles',
    'members.apps.MembersConfig',
    'home.apps.HomeConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'instagram.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'instagram.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# postgres://sltzjerchnoamj:e255ba8e15b1e870edeb2334fb1bc4059e1e5fd401d6038a2608788e9ec93c32@ec2-52-73-155-171.compute-1.amazonaws.com:5432/dfaclajud7pe33
# postgres://vyuaeuvxjkwanr:8412513bd35eddd3922e2d69a431f93c63380ce57b411b6fae2604c02f03db50@ec2-3-224-125-117.compute-1.amazonaws.com:5432/d7jmftv3joabas

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd7jmftv3joabas',
        'USER': 'vyuaeuvxjkwanr',
        'PASSWORD': '8412513bd35eddd3922e2d69a431f93c63380ce57b411b6fae2604c02f03db50',
        'HOST': 'ec2-3-224-125-117.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [




]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = 'static/'


ROOT_PATH = os.path.dirname(__file__)


STATICFILES_DIRS = [os.path.join(ROOT_PATH, 'static')]
FILE_CHARSET = 'utf-8'


LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


cloudinary.config(
    cloud_name="dvua6fhuc",
    api_key="242318296529564",
    api_secret="0l6qjwjrmEFXuT__sbCZgLm1Xyc"
)


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
