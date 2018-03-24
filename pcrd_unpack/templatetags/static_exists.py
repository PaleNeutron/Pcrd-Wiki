from django import template
from django.core.files.storage import default_storage
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.templatetags.staticfiles import static
register = template.Library()

@register.filter
def static_exists(path):
    # path =static(path)
    if finders.find(path[1:].split("/", 1)[1]):
        return True
    else:
        return False