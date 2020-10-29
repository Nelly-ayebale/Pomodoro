import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ayebale:ayebale123@localhost/pomodoro'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'


    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
