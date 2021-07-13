from  .common import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG =os.environ.get("DEBUG") in ['l','t','true','T','True']
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS",'').split(",")

STATICFILES_STORAGE ="moonsoft.settings.storages.StaticAzureStorage" # STATIC 파일 처리 경로
DEFAULT_FILE_STORAGE ="moonsoft.settings.storages.MediaAzureStorage"  #MEDIA 파일 처리 경로

AZURE_ACCOUNT_NAME= os.environ["AZURE_ACCOUNT_NAME"]
AZURE_ACCOUNT_KEY= os.environ["AZURE_ACCOUNT_KEY"]
CKEDITOR_BASEPATH = "https://doubljungdd.blob.core.windows.net/static/ckeditor/ckeditor/"
# AZURE_ACCOUNT_NAME= "doubljungdd"
# AZURE_ACCOUNT_KEY= "iYfhOg65o2dmpHmB6+kG4b2erTEu94xrV1D5YrXKrQu5uwKNRQX0nYNxDIL6g7nwip4o5KVHDnN1vF7rlf8alw=="


# DATABASES = {
#     'default': {
#         "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.postgresql"),
#         "HOST": os.environ["DB_HOST"],
#         "USER": os.environ["DB_USER"],
#         "PASSWORD": os.environ["DB_PASSWORD"],
#         "NAME": os.environ.get("DB_NAME","postgres"),
#     }
# }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

sentry_sdk.init(
    dsn="https://8acdd5ddaa964a2f8bc1ab6ddd70669d@o744598.ingest.sentry.io/5789773",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)