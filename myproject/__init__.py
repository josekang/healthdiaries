import os
from flask import Blueprint, Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message
from flask_login import LoginManager


login_manager = LoginManager()

mail = Mail()

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SECRET_KEY"] = "@#$!@#$%^&*SERTTYBHKJBHFC!@#$%^&*()*&^<%1 id=@QWESDFXCGBHJNJKNBVCSRETYU</%1>"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config['MAIL_USE_TLS'] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = "arigabrian.5@gmail.com"
app.config["MAIL_PASSWORD"] = ""

mail.__init__(app)

db = SQLAlchemy(app)

Migrate(app, db)

login_manager.__init__(app)
login_manager.login_view = "login"


###########################################################
### IMPORT ALL THE BLUEPRINTS #############################
###########################################################
from myproject.contact.views import contact_blueprint
from myproject.user.views import user_blueprint

###########################################################
###### REGISTER THE BLUEPRINTS ############################
###########################################################
app.register_blueprint(contact_blueprint, url_prefix = "/contact")
app.register_blueprint(user_blueprint, url_prefix = "/user")
