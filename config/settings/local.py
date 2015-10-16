"""
Only use this setting for development.

.. Usage::

    python manage.py runserver --settings=config.settings.local
"""

from .common import *


# See: https://docs.djangoproject.com/en/1.8/ref/settings/#debug
DEBUG = True


###################################
# DJANGO DEBUG TOOLBAR
###################################

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)