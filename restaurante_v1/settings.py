"""
Django settings for restaurante_v1 project.
Compatible con Render y entorno local PostgreSQL
"""

from pathlib import Path
import os
import dj_database_url

# -------------------------------
# Rutas y base del proyecto
# -------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------
# Seguridad
# -------------------------------
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-temporal-key')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

# -------------------------------
# Aplicaciones instaladas
# -------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps propias
    'apps.accounts',
    'apps.platillos',
    'apps.ordenes',
    'apps.api',

    # DRF
    'rest_framework',
]

# -------------------------------
# Middleware
# -------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Para Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------------------
# URLs y Templates
# -------------------------------
ROOT_URLCONF = 'restaurante_v1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'restaurante_v1.wsgi.application'

# -------------------------------
# Base de datos
# -------------------------------
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    # Render o cualquier entorno con URL de base de datos
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    }
else:
    # Configuración local
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'restaurante',
            'USER': 'mysite',
            'PASSWORD': 'tu_contraseña_local',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

# -------------------------------
# Autenticación y usuarios
# -------------------------------
AUTH_USER_MODEL = 'accounts.AppUser'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------------
# Internacionalización
# -------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------------------
# Archivos estáticos
# -------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

if not DEBUG:
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -------------------------------
# Configuración DRF
# -------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

# -------------------------------
# Clave por defecto para Render
# -------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
