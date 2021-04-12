import os

os.environ['EMAIL_USER'] = 'adamtesting82@gmail.com'
os.environ['EMAIL_PASS'] = 'thisisfortesting'
os.environ['SECRET_KEY'] = 'f229723ac8d63f2af82f5a9a150d59e6'
os.environ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ec2-user/first_flask_python/flask/flaskblog/site.db'

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')