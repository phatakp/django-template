from .common import *

ALLOWED_HOSTS = []


if DEBUG:
    try:
        from .development import *
    except ImportError:
        print('Production Settings Loaded')
