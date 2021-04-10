import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

os.environ['username2'] = 'adamtesting82@gmail.com'
os.environ['password2'] = 'thisisfortesting'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f229723ac8d63f2af82f5a9a150d59e6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
print(os.environ.get('username2'))
print(os.environ.get('password2'))
app.config['MAIL_USERNAME'] = os.environ.get('username2')
app.config['MAIL_PASSWORD'] = os.environ.get('password2')
mail = Mail(app)

from flaskblog import routes