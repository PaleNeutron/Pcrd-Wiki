import os
from django import template
from django.core.files.storage import default_storage
from django.contrib.staticfiles import finders
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
register = template.Library()

@register.filter
def static_exists(path):
    srt = settings.STATIC_ROOT
    if finders.find(path[1:].split("/", 1)[1]) or os.path.exists(os.path.join(srt, path[1:])):
        return True
    else:
        return False

@register.filter
def escape_return(string):
    # path =static(path)
    return string.replace("\\n", "\n")