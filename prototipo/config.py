class Config(object):
    SECRET_KEY = 'clavesupersecreta100porcientosegurarealnofake'

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'gestordepedidos1234@gmail.com'
    MAIL_PASSWORD = 'Daniel_123'