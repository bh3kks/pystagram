"""
Django settings for pystagram project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z)9(n%e+=rtz4%6w^mxw2a)46qc%qrg^4qcnny@zg*q%2mt*&l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'photo',
    'profiles',)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pystagram.urls'

WSGI_APPLICATION = 'pystagram.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# 웹 페이지에서 사용할 정적 파일의 최상위 URL 경로
STATIC_URL = '/static/'

# 개발 단계에서 사용하는 정적 파일이 위치한 경로들을 지정
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아넣는 경로
# collectstatic 수행시 해당 위치로 복사
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_statics')


# MEDIA - 이용자가 업로드한 파일의 경로 지정
# 웹 페이지에서 사용할 업드라 파일의 최상위 URL 경로
MEDIA_URL = '/uploaded/'

# 업로드 파일의 최상위 경로
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploaded_files')

LOGIN_URL = '/login/'

# 로그인 관련 - 로그인을 하면 사진 업로드 화면으로 이동
#LOGIN_REDIRECT_URL = '/photo/upload/'
