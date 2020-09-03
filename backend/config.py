import os

_KEY_SIZE = 64

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = b'w@W6>sJZp+f!JXf^P;pg{&PgfjaZ4$wQp(;lb|@(+Ht^e??u$f}6MIDsrd(NHfex'
    DATA_UPLOAD = "data/upload"
    DATA_DOWNLOAD = "data/download"
    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    HOST = 'localhost'
    PORT = 8123
    SECRET_KEY = os.urandom(_KEY_SIZE)
    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    HOST = 'localhost'
    PORT = 8123
    SECRET_KEY = os.urandom(_KEY_SIZE)
    SESSION_COOKIE_SECURE = False