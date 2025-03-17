from django import template
from urllib.parse import urlparse

register = template.Library()

@register.filter
def strip_http(value):
    """
    Removes the scheme (http:// or https://) from a URL.
    """
    parsed_url = urlparse(value)
    return parsed_url.netloc if parsed_url.netloc else value
