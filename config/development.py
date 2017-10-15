from config.default import Config


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:test@localhost/luxorv_auth"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
