#서버환경 담당용
from .base import *


STATIC_ROOT = BASE_DIR / 'static/'
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
DEBUG = True