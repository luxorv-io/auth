# Configuration definition
from config import BASE_PATH


class Config(object):
    BASE_DIR = BASE_PATH
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'