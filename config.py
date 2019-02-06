# config.py

class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    TESTING = True          # activates the testing mode of Flask extensions
    DEBUG = True            # activates debug mode in flask
    SQLALCHEMY_ECHO = True  # allows sqlAlchemy to log errors


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}