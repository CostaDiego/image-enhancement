import os

_KEY_SIZE = 64

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = b'w@W6>sJZp+f!JXf^P;pg{&PgfjaZ4$wQp(;lb|@(+Ht^e??u$f}6MIDsrd(NHfex'
    UPLOAD_DIRECTORY = "data/upload"
    DOWNLOAD_DIRECTORY = "data/download"
    SESSION_COOKIE_SECURE = True
    THREADED = True

class ProductionConfig(Config):
    HOST = 'localhost'
    PORT = 5000
    URL = 'http://{host}:{port}'.format(
        host = HOST,
        port = PORT
    )
    SECRET_KEY = os.urandom(_KEY_SIZE)

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    HOST = 'localhost'
    PORT = 8080
    URL = 'http://{host}:{port}'.format(
        host = HOST,
        port = PORT
    )
    SECRET_KEY = os.urandom(_KEY_SIZE)
    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    HOST = 'localhost'
    PORT = 8080
    URL = 'http://{host}:{port}'.format(
        host = HOST,
        port = PORT
    )
    SECRET_KEY = os.urandom(_KEY_SIZE)
    SESSION_COOKIE_SECURE = False