from pathlib import Path
import os

# --------------Base and Template Dir ---------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
# ----------------------------------------------------------------------------------
SECRET_KEY = 'django-insecure-$%_)#k2#*aw^#-k!q_8!1@ns)=4!o!=mcf=-+03vm31y7$d7y_'

DEBUG = True

ALLOWED_HOSTS = []

# -----------------------------Application definition-----------------------------------

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Applications

    "src.website.apps.WebsiteConfig",
    "src.accounts.apps.AccountsConfig",

    # Allauth
    'allauth',
    'allauth.account',
    "allauth.socialaccount",

    # Packages
    'django_countries',
    'crispy_forms',
    'django_filters',
    'widget_tweaks',
]
# ------------------------------------------------------------------------------
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# --------------------------------MiddleWares------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# ---------------------------------------------------------------------------------
ROOT_URLCONF = 'core.urls'

# ------------------------Template Settings-------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'core.wsgi.application'

# --------------------------- Database -----------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------------Password validation-----------------------------------

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

# -------------------Internationalization---------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# -----------------Static and Media setting----------------------------

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --------------------Django Auth Setting--------------------------------

AUTH_USER_MODEL = 'accounts.User'
LOGOUT_REDIRECT_URL = 'account_login'
LOGIN_REDIRECT_URL = 'portal:dashboard'
LOGIN_URL = 'account_login'

# --------------------Django Allauth  Setting--------------------------------

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGOUT_REDIRECT_URL = LOGOUT_REDIRECT_URL
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = None
