import os
from flask import Blueprint, Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message

basedir = os.path.abspath(os.path.dirname(__file__))

mail = Mail()

app = Flask(__name__)

app.config["SECRET_KEY"] = "@#$!@#$%^&*SERTTYBHKJBHFC!@#$%^&*()*&^<%1 id=@QWESDFXCGBHJNJKNBVCSRETYU</%1>"
app.config["SQLALCHEMY_DATABASE_URI"] = "///sqlite" + os.path.join(basedir, "sqlite.data")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config['MAIL_USE_TLS'] = False
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "arigabrian.5@gmail.com"


db = SQLAlchemy(app)

Migrate(app, db)

mail.__init__(app)


###########################################################
### IMPORT ALL THE BLUEPRINTS #############################
###########################################################
from myproject.contact.views import contact_blueprint


###########################################################
###### REGISTER THE BLUEPRINTS ############################
###########################################################
app.register_blueprint(contact_blueprint, url_prefix = "/contact")
