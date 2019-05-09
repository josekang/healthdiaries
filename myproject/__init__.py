import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config["SECRET_KEY"] = "@#$!@#$%^&*SERTTYBHKJBHFC!@#$%^&*()*&^<%1 id=@QWESDFXCGBHJNJKNBVCSRETYU</%1>"
app.config["SQLALCHEMY_DATABASE_URI"] = "///sqlite" + os.path.join(basedir, "sqlite.data")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

Migrate(app, db)
