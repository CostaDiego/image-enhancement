class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "w@W6>sJZp+f!JXf^P;pg{&PgfjaZ4$wQp(;lb|@(+Ht^e??u$f}6MIDsrd(NHfex"

    DATA_UPLOAD = "data/upload"
    DATA_DOWNLOAD = "data/download"

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    DEBUG = True
    TESTING = True

    SESSION_COOKIE_SECURE = False