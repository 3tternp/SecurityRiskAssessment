"""
ASGI configuration for the sraToolDjango project.

This module defines the ASGI callable that serves as the entry point
for asynchronous web servers.

For comprehensive details, refer to the official Django documentation:
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Configure Django's settings module.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sraToolDjango.settings")

# Create and expose the ASGI application instance.
application = get_asgi_application()
