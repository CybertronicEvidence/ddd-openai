##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}