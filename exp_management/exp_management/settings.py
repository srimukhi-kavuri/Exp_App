"""
Django settings for exp_management project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8dl=z@u669!xap)r54aybmit+)zn-ai9i^wmb842!60n*@)o5q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'exp_app',
    'corsheaders',
]

CORS_ORIGIN_ALLOW_ALL=True

# Application definition
CORS_ORIGIN_WHITELIST = (
 'google.com',
 'ec2-3-16-154-211.us-east-2.compute.amazonaws.com:9000/',
 'http://ec2-3-16-154-211.us-east-2.compute.amazonaws.com:9000/',
 '3.16.154.211:9000/',
 '127.0.0.1:9000',
 '*',
 'http://3.16.122.10:8019',
 '3.16.122.10:8019',
 'http://ec2-3-16-122-10.us-east-2.compute.amazonaws.com:8019/',
 'ec2-3-16-122-10.us-east-2.compute.amazonaws.com:8019/',
 'localhost:3000',
 'http://localhost:3000',
 'http://127.0.0.1:3000',
 '127.0.0.1:3000',
 'localhost:3000',
 'localhost:8080',
 'http://3.16.122.10:8011',
 'http://3.16.122.10:8019',
 '3.16.122.10:8019',
 '3.16.122.10:8011',
 'localhost:3001',
 'kapittx-dev-127251261.us-east-2.elb.amazonaws.com:8011',
 'kapittx-dev-127251261.us-east-2.elb.amazonaws.com:8012',
 'kapittx-dev-127251261.us-east-2.elb.amazonaws.com:8019',
 'kapittx-dev-127251261.us-east-2.elb.amazonaws.com:8015',
 'http://ec2-3-16-122-10.us-east-2.compute.amazonaws.com:8011/',
 'ec2-3-16-122-10.us-east-2.compute.amazonaws.com:8011/',
 'http://kapittx-dev-127251261.us-east-2.elb.amazonaws.com:8080',
 'kapittx-dev-127251261.us-east-2.elb.amazonaws.com:8080',
 'ec2-3-19-215-125.us-east-2.compute.amazonaws.com:8011',
 'ec2-3-19-215-125.us-east-2.compute.amazonaws.com:8012',
 'ec2-3-19-215-125.us-east-2.compute.amazonaws.com:8015',
 'ec2-3-19-215-125.us-east-2.compute.amazonaws.com:8019',
 'ec2-3-19-215-125.us-east-2.compute.amazonaws.com:8080',
 'ec2-13-58-231-37.us-east-2.compute.amazonaws.com:8007',
 '00d858d9.ngrok.io',
 'https://00d858d9.ngrok.io/',
 'ec2-13-58-231-37.us-east-2.compute.amazonaws.com:8011',
 'ec2-13-58-231-37.us-east-2.compute.amazonaws.com:9000',
 'ec2-13-58-231-37.us-east-2.compute.amazonaws.com:8011',
 'ec2-13-58-231-37.us-east-2.compute.amazonaws.com:8012',
 'ec2-13-58-231-37.us-east-2.compute.amazonaws.com:8015',
 'ec2-13-58-231-37.us-east-2.compute.amazonaws.com:8019',
 'ec2-13-58-231-37.us-east-2.compute.amazonaws.com:8080',
 'ec2-13-58-231-37.us-east-2.compute.amazonaws.com:8011',
 'ec2-13-58-231-37.us-east-2.compute.amazonaws.com:9000')

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

MIDDLEWARE = [
    #'FAQ.middleware.SessionRedis',
    # 'FAQ.middleware.SessionIdleTimeout',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware'
    # 'FAQ_templates.middleware.AutoLogout',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'exp_management.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'exp_management.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'


##############################email conf####################