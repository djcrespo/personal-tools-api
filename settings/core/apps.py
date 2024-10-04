# LIBRERÍAS DE DJANGO

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# LIBRERÍA DE TERCEROS

THIRD_APPS = [
  'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
    'corsheaders',
    'django_filters',
    'storages'
]

# Apps o módulos del proyecto

LOCAL_APPS = [
    'apps.videos',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + LOCAL_APPS
