from config.default import Config


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://luxorv:p@ssw0d!!@localhost/test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
