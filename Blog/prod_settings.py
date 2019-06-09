import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w9@55$952^cnlakx8(8n3%89t9)0++0p&!(o(p0@(w2p0hd0a+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["194.58.102.17"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog',
        'USER': 'rado',
        'PASSWORD': 'Bt24p6',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


#STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]