"""
WSGI configuration for the sraToolDjango project.

This module defines the WSGI application callable that serves as the entry point
for web servers.

For comprehensive details, refer to the official Django documentation:
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Configure Django's settings module.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sraToolDjango.settings")

# Create and expose the WSGI application instance.
application = get_wsgi_application()
