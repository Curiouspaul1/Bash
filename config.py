import os
from flask import current_app,url_for

dbpassword = os.getenv('dbpassword')

class Config:
	SQLALCHEMY_TRACK_MODIFICATIONS=False
	MAIL_SERVER= 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	MAIL_DEFAULT_SENDER = 'Bammy COllege'
	UPLOADED_IMAGES_DEST = os.getcwd()+"\\bammysite\\static\\uploads"
	SSL_REDIRECT = False
	#UPLOADED_IMAGES_URL = "localhost:5000/images"

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.getenv('DEV_URI') or f"mysql://root:{dbpassword}@localhost/bammy"
	DEBUG=True

class TestingConfig(Config):
    TESTING = True
    #SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_URI') or f"mysql://root:{'dbpassword'}@localhost/bammy_test"
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_URI') or f"mysql://root:{dbpassword}@localhost/bammy_test"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
	UPLOADED_IMAGES_DEST = os.getcwd()+"bammysite/static/uploads"

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,

    'default' : DevelopmentConfig
}


