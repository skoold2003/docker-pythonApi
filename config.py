class Config(object):
    SECRET_KEY = 'pdap'    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):    
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pd@pU53r@localhost/pdap'

class DevelopmentDockerConfig(Config):    
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pd@pU53r@db/pdap'

class TestingConfig(Config):   
    DEBUG = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pd@pU53r@localhost:3310/pdap'

class ProductionConfig(Config):   
    DEBUG = False

config_classes = {
    "development": DevelopmentConfig,
    "development-docker": DevelopmentDockerConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
