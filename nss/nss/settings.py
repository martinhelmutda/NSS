"""
#Last modified by César Buenfil on Oct 19,2018

Django settings for nss project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
pip install django-embed-video

#pip install bcrypt
#pip install django[argon2]

#For images
#pip install pillow

#pip install django-ckeditor
pip install python-social-auth[django]
pip install django-braces
"""


import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE_DIR = os.path.join(BASE_DIR,"templates") #Creo una variable con el path apuntando a mi carpeta templates
PROJECT_TEMPLATE_DIR = os.path.join(BASE_DIR, 'project_app', 'template')

STATIC_DIR=os.path.join(BASE_DIR,"static")
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_URL="/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

print(__file__)
print(TEMPLATE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0%)(4@r51bxp5#3l)19aj6%dzvcobm_w97k@wypfo)s0*+s^8r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

##proyecto
    'account_app',
    'embed_video',
    'ckeditor',
    # 'projects.apps.ProjectsConfig',
    'project_app',

    'search_app',
    'profiles_app',
    'messages_app',
    #SOCIAL AUTH
    'social_django',

]

#AUTHENTIFICATION BACKENDS
AUTHENTICATION_BACKENDS = [
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',

    'django.contrib.auth.backends.ModelBackend',
    #'account_app.authentication.EmailAuthbackend',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware', #SOCIAL
]

ROOT_URLCONF = 'nss.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, MEDIA_ROOT, PROJECT_TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'nss.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

"""
PRODUCTION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kunigo',
        'USER': 'cesar',
        'PASSWORD': 'Linetes13',
        'HOST': '138.68.28.164',
        'PORT': '',
    }
} #pip install django psycopg2
"""

"""
development
"""

DATABASES = {                                   #Nos conectamos a la base de datos mySQL
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kunigo',
        'USER': 'root',
        'PASSWORD': 'toor',
        'HOST': '127.0.0.1',
        #'HOST': '192.168.64.2',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
        'TEST': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'test_kunigo',
        },
    }
}

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

"""


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

# PASSWORD_HASHERS = [
#     'django.contrib.auth.hashers.Argon2PasswordHasher',
#     'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
#     'django.contrib.auth.hashers.BCryptPasswordHasher',
#     'django.contrib.auth.hashers.PBKDF2PasswordHasher',
#     'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
# ]

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'es-mx'#'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOCALE_PATHS = [
    os.path.join(BASE_DIR,'locale')
]

LANGUAGES =[
    ('en','English'),
    ('es-mx','Espanol'),
    ('it','Italiano')

]

DATE_INPUT_FORMATS = [
    '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', # '2006-10-25', '10/25/2006', '10/25/06'
    '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
    '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
    '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
    ]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
                  STATIC_DIR,
                  ]

CRISPY_TEMPLATE_PACK = 'semantic-ui'

LOGIN_URL = 'account_app:user_login'

# LOGIN_REDIRECT_URL ='index'

# PARA EL MAIL Y EL RESET
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


#SOCIAL API AND KEY
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '61695347607-ip2fcoqo7c4tosf8cjq1vraqmcoanuo0.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'oGAyH6EvUgCEiEIN5PJt6kmN'
