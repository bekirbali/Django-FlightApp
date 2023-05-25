from .base import *
from .development import *

from decouple import config

ENVIRONMENT = config('ENV')

if ENVIRONMENT == 'development':
    from .development import *
else:
    from .production import *