from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import Email, ValidationError, DataRequired


class ContactForm(FlaskForm):
    name=TextField("Name", validators=[DataRequired("The name field cannot be empty")])
    email=TextField("Email", validators=[DataRequired(), Email("Enter a valid email address")])
    subject=TextField("Subject")
    message=TextAreaField("Message", validators=[DataRequired("The message field cannot be empty")])
    submit=SubmitField("SEND")
