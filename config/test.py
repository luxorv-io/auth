from config.default import Config


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://test:password@localhost/test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False