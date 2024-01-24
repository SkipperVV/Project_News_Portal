import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"
ROOT_URLCONF = "News_Portal.urls"

CACHES = {
    "default": {
        #'TIMEOUT': 60, # добавляем стандартное время ожидания в минуту (по умолчанию это 5 минут — 300 секунд)
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": os.path.join(
            BASE_DIR, "cache_files"
        ),  # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
        "TIMEOUT": 30,
    }
}

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory' #Приветственное письмо вновьзарегистрировавшемуся товарищу
ACCOUNT_EMAIL_VERIFICATION = "none"  # - без проверки

SITE_ID = 1

ACCOUNT_FORMS = {"signup": "sign.models.BasicSignupForm"}

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv(
    "EMAIL_HOST_PASSWORD"
)  # mail.ru пароль для внешнего приложения
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True

ADMINS = {'admin', 'skippervasin@gmail.com'}

SERVER_EMAIL = DEFAULT_FROM_EMAIL

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"  # все уведомления будут приходить в консоль.
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'#Чтобы уведомления приходили на почту

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

CELERY_BROKER_URL = "redis://localhost:6379"  #'redis-10049.c100.us-east-1-4.ec2.cloud.redislabs.com:10049'#
CELERY_RESULT_BACKEND = "redis://localhost:6379"  #'redis-10049.c100.us-east-1-4.ec2.cloud.redislabs.com:10049'#
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

# формат даты, которую будет воспринимать наш задачник
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
# если задача не выполняется за 25 секунд, то она автоматически снимается
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

import logging

logger = logging.getLogger("django")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "style": "{",
    # -----filters-------------------------------------------------    
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        }        
    },
    # -----formatters-------------------------------------------------
    "formatters": {
        "DEBUG_log": {
            # все сообщения уровня DEBUG и выше, включающие время, уровень сообщения, сообщения.
            "format": "%(asctime)s - %(levelname)s, Message: %(message)s",
        },
        "INFO_log": {
            # все сообщения уровня DEBUG и дополнительно должен выводиться путь к источнику события.
            "format": '%(asctime)s - %(levelname)s, Module: "%(module)s", Message: %(message)s',
        },
        "WARNING_log": {
            # сообщений WARNING и выше дополнительно должен выводиться путь к источнику события
            # (используется аргумент pathname в форматировании
            "format": "Path %(pathname)s",
        },
        "ERROR_log": {
            # для сообщений ERROR и CRITICAL еще должен выводить
            # стэк ошибки (аргумент exc_info)
            "format": "%(asctime)s, %(levelname)s, %(pathname)s, %(message)s, %(exc_info)s",
        },
    },
    # ----handlers--------------------------------------------------
    "handlers": {
        "console": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "DEBUG_log",
        },
        "console_warning": {
            "level": "WARNING",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "WARNING_log",
        },
        # с указанием времени, уровня логирования, модуля, в котором возникло сообщение (аргумент module) и само сообщение
        "general_log_file": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.FileHandler",
            "formatter": "INFO_log",
            "filename": "general.log",
        },
        "warning_to_file": {
            "level": "WARNING",
            "filters": ["require_debug_false"],
            "class": "logging.FileHandler",
            "formatter": "WARNING_log",
            "filename": "general.log",
        },
        "errors_log_file": {
            "level": "ERROR", #"INFO", for test
            "class": "logging.FileHandler",
            "formatter": "ERROR_log",
            "filename": "errors.log",
        },
        "security_log_file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "formatter": "ERROR_log",
            "filename": "security.log",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],            
            "class": "django.utils.log.AdminEmailHandler",
            "email_backend": "django.core.mail.backends.filebased.EmailBackend",
            "formatter": "ERROR_log",
        },
    },
    # -----loggers-------------------------------------------------
    "loggers": {
        "django": {
            "handlers": [
                "console",
                "console_warning",
                "general_log_file",
                "warning_to_file",
            ],
            "propagate": True,
        },
        "django.template": {
            "handlers": ["errors_log_file"],
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["errors_log_file"],
            "propagate": False,
        },
        "django.server": {
            "handlers": ["mail_admins", "errors_log_file"],
            "propagate": True,
        },
        "django.request": {
            "handlers": ["mail_admins", "errors_log_file"],
            "propagate": False,
        },
        "django.security": {
            "handlers": ["security_log_file"],  
            "propagate": False,
        },
    },
}
# Application definition

INSTALLED_APPS = [
    'modeltranslation', # транслятор обязательно вставить перед админом
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Models.apps.ModelsConfig",
    "django.contrib.sites",
    "django.contrib.flatpages",
    "django_filters",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",   # ... include the providers you want to enable:
    "sign",
    "protect",
    "django_apscheduler",     # отправлять периодические письма
    'rest_framework', # нужно добавить Django REST Framework в список установленных приложений
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    'django.middleware.locale.LocaleMiddleware', # Для пакета gettext 0.21
    'basic.middlewares.TimezoneMiddleware', # Запрос на локальное время пользователя
    # Cashing of the Full site:
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
                # `allauth` needs this from django
                "django.template.context_processors.request",
            ],
        },
    },
]
# Теперь все наши запросы по умолчанию будут доступны только авторизованным пользователям.
REST_FRAMEWORK = {
   'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
   'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
   'PAGE_SIZE': 10,
   'DEFAULT_PERMISSION_CLASSES': [
       'rest_framework.permissions.IsAuthenticated',
   ]

}

WSGI_APPLICATION = "News_Portal.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

#LANGUAGE_CODE = "en-us"
LANGUAGE_CODE = 'ru'
LANGUAGES = [
    ('ru','Русский'),
    ('en-us', 'English')
    ]
USE_I18N = True
TIME_ZONE = "UTC"
USE_TZ = False
SITE_ID = 1
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
SITE_URL = "http://127.0.0.1:8000"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
