import os

class Config(object):
    DEBUG = False
    SECRET_KEY = '5602bcb11b65e1b97e86fec9244d832a25a292900bd8bb7786f273b2903aab5076f1e506'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:@localhost:5432/tuneship'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_ENABLE = True

    # Bcrypt alogrith hasing rounds
    BCRYPT_LOG_ROUNDS = 15

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_ENABLE = True

    # Bcrypt alogrith hasing rounds
    BCRYPT_LOG_ROUNDS = 15

    
    