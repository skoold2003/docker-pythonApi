class Config(object):
    SECRET_KEY = 'pdap'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<mysql_user>:<mysql_password>@db/pdap'

class TestingConfig(Config):   
    DEBUG = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<mysql_user>:<mysql_password>@localhost/pdap'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<mysql_user>:<mysql_password>@db/pdap'


config_classes = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}