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