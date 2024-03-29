from log import logger


class Config:
    SECRET_KEY = "secret"
    JWT_SECRET_KEY = "secret"
    CORS_ORIGINS = "*"
    CORS_SUPPORTS_CREDENTIALS = True
    SQLALCHEMY_DATABASE_URI = "DBMS://USERNAME:PASSWORD@HOST_ADD/db_name"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        logger()


class DevelopmentConfig(Config):
    DEBUG = True
    JWT_ACCESS_TOKEN_EXPIRES = False
    JWT_REFRESH_TOKEN_EXPIRES = False


class ProductionConfig(Config):
    JWT_ACCESS_TOKEN_EXPIRES = 3600
