from ._base import *

# Enter all production settings here
ALLOWED_HOSTS = []

if DEBUG:
    try:
        from .local import *
        print('Running Local Settings')
    except ImportError:
        print('Running Production Settings')
