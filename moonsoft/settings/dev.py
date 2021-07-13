from  .common import *
import sentry_sdk
from decouple import config
from sentry_sdk.integrations.django import DjangoIntegration

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
# DATABASES = {
#     'default': {
#         'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('POSTGRES_NAME'),
#         'USER': config('POSTGRES_USER'),
#         'PASSWORD': config('POSTGRES_PASSWORD'),
#         'HOST': config('POSTGRES_HOST'),
#         'PORT': config('POSTGRES_PORT'),
#     }
#     }
# }

