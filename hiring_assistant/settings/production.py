from decouple import config

from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [config('ALLOWED_HOSTS')]

# SendGrid configuration
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = config('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = config('SENDGRID_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True