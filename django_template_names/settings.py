from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-ksh9^l!g(y07-p20hwx%cdu_4-m2=bpp=q3xx)(%#m9-+k^y$7'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = ['template_names.apps.TemplateNamesConfig']

MIDDLEWARE = []

ROOT_URLCONF = 'django_template_names.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
    },
]
