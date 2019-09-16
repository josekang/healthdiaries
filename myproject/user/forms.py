#################################################
#### CREATE THE IMPORTS FOR THE USER FORM #######
#################################################

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.validators import ValidationError
from myproject.user.models import User

#################################################
#### NOW CREATE THE FORMS FOR THE USER ##########
#################################################

class LoginUserForm(FlaskForm):
    email = StringField("Enter Your Email ", validators = [DataRequired(), Email("Enter a valid email")])
    password = PasswordField("Enter Your Password ", validators = [DataRequired("The password field is either empty or you have entered the wrong password")])
    submit = SubmitField("SIGN IN")


class RegisterUserForm(FlaskForm):
    email = StringField("Enter Your Email ", validators = [DataRequired(), Email("Enter a valid email")])
    username = StringField("Enter Your Username ", validators = [DataRequired("The username field cannot be empty")])
    password = PasswordField("Choose a strong password ", validators = [DataRequired(), EqualTo("confirm_password", message = "The password do not match")])
    confirm_password = PasswordField("Confirm Your Password ", validators = [DataRequired("The confirm password cannot be empty or it does not match the password field")])
    submit = SubmitField("SIGN UP")

    def check_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError("The eamil has already been registerd!!!")

    def check_username(self, field):
        if User.query.filter_by(username = field.data):
            raise ValidationError("The username has already been registerd!!!")
